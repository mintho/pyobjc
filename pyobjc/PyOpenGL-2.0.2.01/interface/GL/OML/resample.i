/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module resample

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.OML.resample Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_OML_resample)

#endif
%}

/* FUNCTION DECLARATIONS */


/* CONSTANT DECLARATIONS */
#define           GL_PACK_RESAMPLE_OML 0x8984
#define         GL_UNPACK_RESAMPLE_OML 0x8985
#define      GL_RESAMPLE_REPLICATE_OML 0x8986
#define      GL_RESAMPLE_ZERO_FILL_OML 0x8987
#define        GL_RESAMPLE_AVERAGE_OML 0x8988
#define       GL_RESAMPLE_DECIMATE_OML 0x8989


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_OML_resample)

#endif
	NULL
};

#define glInitResampleOML() InitExtension("GL_OML_resample", proc_names)
%}

int glInitResampleOML();
DOC(glInitResampleOML, "glInitResampleOML() -> bool")

%{
PyObject *__info()
{
	if (glInitResampleOML())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
