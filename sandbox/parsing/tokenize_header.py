from scanner import *
from textwrap import dedent


SUBPATTERNS = dict(
    AVAILABLE=r'([A-Z][A-Z0-9_]+)',
    PROTOCOLS=r'(<[^>]+>)',
    KEYWORD=r'((double|float|int|unsigned|long|char|extern|volatile|void|inline|__(\w+?)__|const|typedef|static|const))',
    IDENTIFIER=r'([A-Za-z_]\w*)',
    SIZEOF=r'(sizeof\(([^)]+)\))',
    DECIMAL=r'([+\-]?((\.\d+)|(\d+(\.\d*)?))([eE]\d+)?[fF]?)',
    INTEGER=r'([+\-]?\d+[uU]?[lL]?)',
    CHARS=r"('([^\\'\n]|\\')*')",
    STRING=r'("([^\\"\n]|\\")*")',
    CFSTRING=r'(CFSTR\("([^\\"\n]|\\")*"\))',
    HEX=r'(0[xX][0-9a-fA-F]+[lL]?)',
    EXTERN=r'((([A-Z-a-z_]\w*?_)?(EXTERN|EXPORT)|extern))',
    EXPORT=r'((([A-Z-a-z_]\w*?_)?(EXPORT|EXTERN)|extern))',
    STATIC_INLINE=r'((([A-Z-a-z_]\w*?_)?INLINE|static\sinline|static\s__inline__))',
    BRACES=r'(([^\n}]*|([^}][^\n]*\n)*))',
    INDIRECTION=r'(\s*\*)',
    BOL=r'(\s*^\s*)',
    EOL=r'(\s*$\n?)',
)

def deadspace(string, begin, end):
    return 'NO MATCH FOR [%d:%d] %r' % (begin, end, string[begin:end])

def pattern(s):
    return dedent(s).strip() % SUBPATTERNS

def example(s):
    return dedent(s).strip()

class CPPDecls(Token):
    pattern = pattern(r'''
    (__BEGIN_DECLS|__END_DECLS)
    ''')

class CPPCrap(Token):
    pattern = pattern(r'''
    \#\s*(
        if\s*defined\s*\(\s*__cplusplus\s*\)
        | ifdef\s*__cplusplus
    )
    (?P<body>
        [^#]*
        (
            \#if[^#]*
            (
                (?!\#\s*endif)
                \#
                [^#]*
            )*
            \#\s*endif[^#]*

          |
            (?!\#\s*endif)
            \#
            [^#]*
        )*
    )
    \#\s*endif
    ''')
    example = example('''
    #if defined(__cplusplus)
    extern "C" {
    #endif
    #if defined(__cplusplus)
    }
    #endif
    #ifdef __cplusplus
    sucktastic
    #define foo
    #endif
    ''')

class BlockComment(Token):
    pattern = pattern(r'''
    \/\*
    (?P<comment>([^*]|\*(?!/))*)
    \*\/
    ''')
    example = example('''
    /*************\t\tThis is an annoying one\t\t**********/
    /* this is a block comment */
    ''')

class SingleLineComment(Token):
    pattern = pattern(r'//(?P<comment>[^\n]*)(\n|$)')
    example = example(r'// this is a single line comment')

class UninterestingTypedef(Token):
    pattern = pattern(r'''
    typedef
    \s*(?P<body>[^;]*)
    ;
    ''')
    example = example('''
    typedef baz wibble fun* SomethingGreat;
    ''')

class CompilerDirective(Token):
    pattern = pattern(r'''
    \#\s*(?P<name>undef|if|ifdef|ifndef|endif|else|elif|pragma|error|warn|define)
    [ \t]*(?P<body>([^\\\n]|\\(\n|$))*)
    ''')
    example = example(r'''
    #if defined(foo)
    #if \
        insane
    #endif
    #else stuff
    #define NS_DURING { \
        GARBAGE!  blah blah {
    ''')

class Interface(Token):
    pattern = pattern(r'''
    @interface
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:\((?P<category>%(IDENTIFIER)s)\))?
        \s*(?::\s*(?P<super>%(IDENTIFIER)s))?
        \s*(?:<(?P<protocols>[^>]*)>)?
        \s*(?:{(?P<ivars>%(BRACES)s)})?
        \s*(?P<interface_body>.*?)
    @end
    ''')
    example = example(r'''
    @interface Foo(Bar): Baz <protocols> {
    @private
        NSArray *crazy;
    }

    + (Foo *)newFoo;
    - init;
    @end
    ''')

class Protocol(Token):
    pattern = pattern(r'''
    @protocol
        \s+(?P<name>%(IDENTIFIER)s)
        \s*(?:<(?P<super>%(IDENTIFIER)s)>)?
        \s*(?P<protocol_body>.*?)
    @end
    ''')
    example = example(r'''
    @protocol FooProtocol <Foo>
    + (Foo *)protoFoo;
    @end
    ''')

class AngleImport(Token):
    pattern = pattern(r'''
    \#\s*(?P<import_type>import|include)
        \s+<(?P<import_file>[^>]*)>
    ''')
    example = example('#import <Foo/Bar.h>')

class StringImport(Token):
    pattern = pattern(r'''
    \#\s*(?P<import_type>import|include)
        \s+"(?P<import_file>[^"]*)"
    ''')
    example = example('#import "Foo/Bar.h"')

class SimpleDefine(Token):
    # XXX foo << bar
    # XXX foo | bar | baz
    # XXX ((type)foo)
    pattern = pattern(r'''
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)\s+
        \(?
            (?P<value>
                (?!%(KEYWORD)s)
                (
                    %(CFSTRING)s
                    | %(CHARS)s
                    | %(STRING)s
                    | %(HEX)s
                    | %(DECIMAL)s
                    | %(INTEGER)s
                    | %(SIZEOF)s
                    | %(IDENTIFIER)s
                )
            )
        \)?
        (?!
            [ \t]*[^/\n \t]
        )
    ''')
    example = example(r'''
    #define foo 'foo!'
    #define foo bar
    #define foo 0x200
    #define foo 2.0
    #define foo "foo"
    #define foo CFSTR("foo")
    #define foo sizeof(bar)
    #define foo (8)
    ''')
    
class MacroDefine(Token):
    pattern = pattern(r'''
    \#\s*define\s*
        (?P<name>%(IDENTIFIER)s)
        \s*\(
            (?P<args>
                (\s*%(IDENTIFIER)s\s*,)*
                (\s*%(IDENTIFIER)s\s*)?
            )
        \)
    \s*(?P<body>([^\\\n]|\\(\n|$))*)
    ''')
    example = example(r'''
    #define NSLocalizedString(key, comment) \
        [[NSBundle mainBundle] localizedStringForKey:(key) value:@"" table:nil]
    #define GetNSApp() [NSApplication sharedApplication]
    #define DoStuff(a, b, c) do { \
        blah blah blah \
        blah blah blah \
    } while (0);
    ''')

class GlobalThing(Token):
    pattern = pattern(r'''
    (?:%(EXTERN)s|%(EXPORT)s)\s+
    (const\s+)?
    (?P<type>%(IDENTIFIER)s%(INDIRECTION)s*)
    \s*(const\s+)?
    (?P<name>
        %(IDENTIFIER)s
        (
            \s*,\s*
            %(INDIRECTION)s*
            \s*(const\s+)?
            %(IDENTIFIER)s
        )*
    )
    (?:\s*\[\s*\]\s*|\b)
    (
        (\s*//(?P<comment>[^\n]*)(\n|$))?
        (?:\s+%(AVAILABLE)s)
    )?
    ;
    ''')
    example = example(r'''
    extern const double FooBar;
    extern const NSString *foo;
    extern NSString *foo;
    APPKIT_EXTERN NSString* const foo;
    APPKIT_EXTERN NSString* const foo // argh a comment
        AVAILABLE_SOMEWHERE;
    FOUNDATION_EXPORT NSString * const Foo;
    extern CFStringRef cfFoo AVAILABLE_MAC_OSX_10_8;
    APPKIT_EXTERN const char foosball[] AVAILABLE_NEVER;
    ''')

class ForwardClassReference(Token):
    pattern = pattern(r'@class (?P<name>[^;]+);')
    example = example(r'@class Foo;')

class EnumBareMember(Token):
    pattern = pattern(r'''
    \s*(?P<name>%(IDENTIFIER)s)
    \s*,?
    ''')
    example = example(r'''
    Foo,
    Foo
    ''')

class EnumValueMember(Token):
    pattern = pattern(r'''
    \s*(?P<name>%(IDENTIFIER)s)
    \s*=
    \s*(?P<value>(
        %(INTEGER)s
        | %(HEX)s
        | %(CHARS)s
        | %(IDENTIFIER)s
        ))
    \s*,?
    ''')
    example = example(r'''
    Foo = 12,
    Foo = 2
    ''')

class NamedEnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*(?P<name>%(IDENTIFIER)s)
    \s*;
    ''')
    example = example(r'''
    } FooBarBazWible;
    ''')

class NamedEnum(ScanningToken):
    pattern = pattern(r'''
    typedef
    \s+enum
    \s*(?P<name>%(IDENTIFIER)s)?
    \s*{\s*
    ''')
    endtoken = NamedEnumEnd
    lexicon = [
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        EnumValueMember,
        EnumBareMember,
    ]
    example = example(r'''
    typedef enum {
        FooBar = 1, // This is the best value for FooBar
        Baz = 2,
        Wibble
    } FooBarBazWibble;
    typedef enum {
        FooBar, /* But this FooBar has no value! */
        Baz,
        Wibble
    } FooBarBazWibble;
    ''')

class EnumEnd(Token):
    pattern = pattern(r'''
    \s*}
    \s*;
    ''')
    example = example(r'''
    };
    ''')

class UninterestingStruct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    struct[^{;]+;
    ''')
    example = example(r'''
    struct Foo;
    struct Foo Bar;
    ''')

 
class Struct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    (struct|union)
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*{
        (?P<content>%(BRACES)s)
    }
    (\s*%(AVAILABLE)s)?
    \s*;
    ''')
    example = example(r'''
    struct {
        signed foo name;
        int bar;
    };
    struct _FooBarStruct {
        signed foo name;
        int bar;
    };
    ''')

class NamedStruct(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    typedef
    \s+(struct|union)
    \s*(?P<structname>%(IDENTIFIER)s)?
    \s*
    {
    (?P<body>%(BRACES)s)
    }
    \s*%(IDENTIFIER)s
    (\s*%(AVAILABLE)s)?
    \s*;
    ''')
    example = example(r'''
    typedef struct {unsigned long v;} NSSwappedFloat;
    typedef struct { int bar; } FooBar;
    typedef struct {
        signed foo name;
        int bar;
    } FooBarStruct;
    typedef struct _FooBarStruct {
        signed foo name;
        int bar;
    } FooBarStruct;
    typedef struct _FooBarStruct {
        signed foo name;
        union {
            int stuff;
        } foo;
        int bar;
    } FooBarStruct;
    ''')
 
class Enum(ScanningToken):
    pattern = pattern(r'''
    \s*enum
    \s*(?P<name>%(IDENTIFIER)s)?
    \s*{\s*
    ''')
    endtoken = EnumEnd
    lexicon = [
        InsignificantWhitespace,
        BlockComment,
        SingleLineComment,
        EnumValueMember,
        EnumBareMember,
    ]
    example = example(r'''
    enum {
        FooBar = 1, // This is the best value for FooBar
        Baz = 2,
        Wibble
    };
    enum {
        FooBar, /* But this FooBar has no value! */
        Baz,
        Wibble
    };
    ''')

class FunctionEnd(Token):
    # XXX - UNUSED
    pattern = pattern(r'''
    \)
    \s*;
    ''')
    example = example(r'''
    );
    )  ;
    ''')

class FunctionParameter(Token):
    # XXX - UNUSED
    pattern = pattern(r'''
    (%(IDENTIFIER)s\s*)+
    \s*%(INDIRECTION)s
    \s*%(IDENTIFIER)s?
    \s*,?\s*
    ''')
    example = example(r'''
    NSString *foo, NSString *bar
    ''')

#class ExportFunction(ScanningToken):
#    pattern = pattern(r'''
#    %(EXPORT)s
#    \s*(?P<returns>%(IDENTIFIER)s%(INDIRECTION)s*)
#    \s*%(IDENTIFIER)s
#    \s*\(
#    ''')
#    endtoken = FunctionEnd
#    lexicon = [
#        InsignificantWhitespace,
#        FunctionParameter,
#    ]
#    example = example(r'''
#    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
#    FOUNDATION_EXPORT SomeResult SomeName(int,float);
#    ''')

class ExportFunction(Token):
    # XXX handle comments? need its own internal parser?
    pattern = pattern(r'''
    %(EXPORT)s?
    \s*(?P<returns>
        (%(KEYWORD)s\s*)*
        %(IDENTIFIER)s
        (%(INDIRECTION)s|\s+%(KEYWORD)s)*
    )
    (\s*(?P<protocols>%(PROTOCOLS)s))?
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
        (?P<args>\s*[^)]*)
    \s*\)
    (\s*(?P<available>%(AVAILABLE)s))?
    \s*;
    ''')
    example = example(r'''
    APPKIT_EXTERN NSString *NSSomething(NSString *arg, NSString *arg)
        AVAILABLE_SOMEWHERE;
    FOUNDATION_EXPORT void *NSSomething(unsigned long arg, unsigned long arg) AVAILABLE_SOMEWHERE;
    FOUNDATION_EXPORT SomeResult <NSObject> SomeName(const Foo *, const Foo *Bar);
    FOUNDATION_EXPORT SomeResult **SomeName(const Foo *, const Foo *Bar);
    FOUNDATION_EXPORT SomeResult SomeName(int,float);
    ''')

class StaticInlineFunction(Token):
    # XXX need to figure out how to find a close brace
    #     will probably need something stateful I guess
    pattern = pattern(r'''
    %(STATIC_INLINE)s
    \s*(?P<returns>
        (%(KEYWORD)s\s*)*
        %(IDENTIFIER)s
        (%(INDIRECTION)s|\s+%(KEYWORD)s)*
    )
    \s*(?P<name>%(IDENTIFIER)s)
    \s*\(
        (?P<args>\s*[^)]*)
    \s*\)
    \s*{
        (?P<body>%(BRACES)s)
    }
    ''')
    example = example(r'''
    static inline unsigned int NSEventMaskFromType(NSEventType type) { return (1 << type); }
    FOUNDATION_STATIC_INLINE BOOL NSDecimalIsNotANumber(const NSDecimal *dcm)
      { return ((dcm->_length == 0) && dcm->_isNegative); }
    FOUNDATION_STATIC_INLINE unsigned short NSSwapShort(unsigned short inv) {
        return CFSwapInt16(inv);
    }
    FOUNDATION_STATIC_INLINE NSSwappedFloat NSConvertHostFloatToSwapped(float x) {
        union fconv {
        float number;
        NSSwappedFloat sf;
        };
        return ((union fconv *)&x)->sf;
    }
    ''')


LEXICON = [
    InsignificantWhitespace,
    BlockComment,
    SingleLineComment,
    Interface,
    Protocol,
    AngleImport,
    StringImport,
    SimpleDefine,
    GlobalThing,
    ForwardClassReference,
    NamedEnum,
    Enum,
    NamedStruct,
    Struct,
    ExportFunction,
    StaticInlineFunction,
    UninterestingTypedef,
    UninterestingStruct,
    MacroDefine,
    CPPDecls,
    CPPCrap,
    CompilerDirective,
]

if __name__ == '__main__':
    from pdb import pm
    import re
    import sys
    frameworks = """
    AddressBook
    AppKit
    ExceptionHandling
    Foundation
    InterfaceBuilder
    Message
    PreferencePanes
    ScreenSaver
    SecurityInterface
    WebKit
    CoreFoundation
    AppKitScripting
    ApplicationServices
    Cocoa
    DirectoryService
    DiscRecording
    DiscRecordingUI
    LDAP
    Scripting
    SecurityFoundation
    SecurityInterface
    System
    SystemConfiguration
    #Security
    #Carbon
    #CoreServices
    """.split()
    files = sys.argv[1:]
    if not files:
        import glob
        for framework in frameworks:
            if framework.startswith('#'):
                continue
            files.extend(glob.glob('/System/Library/Frameworks/%s.framework/Headers/*.h' % (framework,)))
    fn = None
    def deadraise(string, i, j):
        print '-' * len(fn)
        print fn
        print '-' * len(fn)
        s = string[i:].split('\n',1)[0]
        print s
        print
        import pdb
        pdb.Pdb().set_trace()
    scan = Scanner(LEXICON)
    for fn in files:
        print '-' * len(fn)
        print fn
        print '-' * len(fn)
        for token in scan.iterscan(file(fn).read(), dead=deadraise):
            if token is not None:
                print token