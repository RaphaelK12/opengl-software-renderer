# License Applicability. Except to the extent portions of this file are
# made subject to an alternative license as permitted in the SGI Free
# Software License B, Version 1.1 (the "License"), the contents of this
# file are subject only to the provisions of the License. You may not use
# this file except in compliance with the License. You may obtain a copy
# of the License at Silicon Graphics, Inc., attn: Legal Services, 1600
# Amphitheatre Parkway, Mountain View, CA 94043-1351, or at:
#
# http://oss.sgi.com/projects/FreeB
#
# Note that, as provided in the License, the Software is distributed on an
# "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS
# DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND
# CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A
# PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
#
# Original Code. The Original Code is: OpenGL Sample Implementation,
# Version 1.2.1, released January 26, 2000, developed by Silicon Graphics,
# Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc.
# Copyright in any portions created by third parties is as indicated
# elsewhere herein. All Rights Reserved.
#
# Additional Notice Provisions: This software was created using the
# OpenGL(R) version 1.2.1 Sample Implementation published by SGI, but has
# not been independently verified as being compliant with the OpenGL(R)
# version 1.2.1 Specification.
#
# $Date: 2000/04/26 02:10:53 $ $Revision: 1.1 $
# $Header: /home/pub/cvs/projects/ogl-sample/main/doc/registry/specs/glxenum.spec,v 1.1 2000/04/26 02:10:53 ljp Exp $

# This is the GLX enumerant registry.
#
# It is an extremely important file. Do not mess with it unless
# you know what you're doing and have permission to do so.
#
# Rules for modification are the same as the rules for the OpenGL
# enumerant registry (gl.spec). Basically, don't modify this
# file unless you're SGI's ARB Representative.

@@ Add multisample extension
Extensions define:
	VERSION_1_1					= 1
	VERSION_1_2					= 1
	VERSION_1_3					= 1
	SGIS_multisample				= 1
	EXT_visual_info					= 1
	SGI_swap_control				= 1
	SGI_video_sync					= 1
	SGI_make_current_read				= 1
	SGIX_video_source				= 1
	EXT_visual_rating				= 1
	EXT_import_context				= 1
	SGIX_fbconfig					= 1
	SGIX_pbuffer					= 1
	SGI_cushion					= 1
	SGIX_video_resize				= 1
	SGIX_dmbuffer					= 1
	SGIX_swap_group					= 1
	SGIX_swap_barrier				= 1
	SGIS_blended_overlay				= 1
	SGIS_shared_multisample				= 1
	SUN_transparent_index				= 1
	3DFX_multisample				= 1

GLXStringName enum:
	VENDOR						= 0x1
	VERSION						= 0x2
	EXTENSIONS					= 0x3

GLXErrorCode enum:
	BAD_SCREEN					= 1
	BAD_ATTRIBUTE					= 2
	NO_EXTENSION					= 3
	BAD_VISUAL					= 4
	BAD_CONTEXT					= 5
	BAD_VALUE					= 6
	BAD_ENUM					= 7

GLXDrawableTypeMask enum:
	WINDOW_BIT					= 0x00000001	# DRAWABLE_TYPE value
	PIXMAP_BIT					= 0x00000002	#   "
	PBUFFER_BIT					= 0x00000004	#   "
	WINDOW_BIT_SGIX					= 0x00000001	# DRAWABLE_TYPE_SGIX value
	PIXMAP_BIT_SGIX					= 0x00000002	#   "
	PBUFFER_BIT_SGIX				= 0x00000004	#   "

GLXRenderTypeMask enum:
	RGBA_BIT					= 0x00000001	# RENDER_TYPE value
	COLOR_INDEX_BIT					= 0x00000002	#   "
	RGBA_BIT_SGIX					= 0x00000001	# RENDER_TYPE_SGIX value
	COLOR_INDEX_BIT_SGIX				= 0x00000002	#   "

GLXSyncType enum:
	SYNC_FRAME_SGIX					= 0x00000000	# ChannelRectSyncSGIX synctype
	SYNC_SWAP_SGIX					= 0x00000001	#   "

GLXEventMask enum:
	PBUFFER_CLOBBER_MASK				= 0x08000000	# SelectEvent mask
	BUFFER_CLOBBER_MASK_SGIX			= 0x08000000	# SelectEventSGIX mask

GLXPbufferClobberMask enum:
	FRONT_LEFT_BUFFER_BIT				= 0x00000001	# PbufferClobberEvent mask
	FRONT_RIGHT_BUFFER_BIT				= 0x00000002	#   "
	BACK_LEFT_BUFFER_BIT				= 0x00000004	#   "
	BACK_RIGHT_BUFFER_BIT				= 0x00000008	#   "
	AUX_BUFFERS_BIT					= 0x00000010	#   "
	DEPTH_BUFFER_BIT				= 0x00000020	#   "
	STENCIL_BUFFER_BIT				= 0x00000040	#   "
	ACCUM_BUFFER_BIT				= 0x00000080	#   "
	FRONT_LEFT_BUFFER_BIT_SGIX			= 0x00000001	# BufferClobberEventSGIX mask
	FRONT_RIGHT_BUFFER_BIT_SGIX			= 0x00000002	#   "
	BACK_LEFT_BUFFER_BIT_SGIX			= 0x00000004	#   "
	BACK_RIGHT_BUFFER_BIT_SGIX			= 0x00000008	#   "
	AUX_BUFFERS_BIT_SGIX				= 0x00000010	#   "
	DEPTH_BUFFER_BIT_SGIX				= 0x00000020	#   "
	STENCIL_BUFFER_BIT_SGIX				= 0x00000040	#   "
	ACCUM_BUFFER_BIT_SGIX				= 0x00000080	#   "
	SAMPLE_BUFFERS_BIT_SGIX				= 0x00000100	#   "

GLXAttribute enum:
	USE_GL						= 1		# Visual attributes
	BUFFER_SIZE					= 2		#   "
	LEVEL						= 3		#   "
	RGBA						= 4		#   "
	DOUBLEBUFFER					= 5		#   "
	STEREO						= 6		#   "
	AUX_BUFFERS					= 7		#   "
	RED_SIZE					= 8		#   "
	GREEN_SIZE					= 9		#   "
	BLUE_SIZE					= 10		#   "
	ALPHA_SIZE					= 11		#   "
	DEPTH_SIZE					= 12		#   "
	STENCIL_SIZE					= 13		#   "
	ACCUM_RED_SIZE					= 14		#   "
	ACCUM_GREEN_SIZE				= 15		#   "
	ACCUM_BLUE_SIZE					= 16		#   "
	ACCUM_ALPHA_SIZE				= 17		#   "
	CONFIG_CAVEAT					= 0x20		#   "
	X_VISUAL_TYPE					= 0x22		#   "
	TRANSPARENT_TYPE				= 0x23		#   "
	TRANSPARENT_INDEX_VALUE				= 0x24		#   "
	TRANSPARENT_RED_VALUE				= 0x25		#   "
	TRANSPARENT_GREEN_VALUE				= 0x26		#   "
	TRANSPARENT_BLUE_VALUE				= 0x27		#   "
	TRANSPARENT_ALPHA_VALUE				= 0x28		#   "
	DONT_CARE					= 0xFFFFFFFF	# may be specified for ChooseFBConfig attributes
	NONE						= 0x8000	# several attribute values
	SLOW_CONFIG					= 0x8001	# CONFIG_CAVEAT attribute value
	TRUE_COLOR					= 0x8002	# X_VISUAL_TYPE attribute value
	DIRECT_COLOR					= 0x8003	#   "
	PSEUDO_COLOR					= 0x8004	#   "
	STATIC_COLOR					= 0x8005	#   "
	GRAY_SCALE					= 0x8006	#   "
	STATIC_GRAY					= 0x8007	#   "
	TRANSPARENT_RGB					= 0x8008	# TRANSPARENT_TYPE attribute value
	TRANSPARENT_INDEX				= 0x8009	#   "
	VISUAL_ID					= 0x800B	# Context attribute
	SCREEN						= 0x800C	#   "
	NON_CONFORMANT_CONFIG				= 0x800D	# CONFIG_CAVEAT attribute value
	DRAWABLE_TYPE					= 0x8010	# FBConfig attribute
	RENDER_TYPE					= 0x8011	#   "
	X_RENDERABLE					= 0x8012	#   "
	FBCONFIG_ID					= 0x8013	#   "
	RGBA_TYPE					= 0x8014	# CreateNewContext render_type value
	COLOR_INDEX_TYPE				= 0x8015	#   "
	MAX_PBUFFER_WIDTH				= 0x8016	# FBConfig attribute
	MAX_PBUFFER_HEIGHT				= 0x8017	#   "
	MAX_PBUFFER_PIXELS				= 0x8018	#   "
	PRESERVED_CONTENTS				= 0x801B	# CreateGLXPbuffer attribute
	LARGEST_PBUFFER					= 0x801C	#   "
	WIDTH						= 0x801D	# Drawable attribute
	HEIGHT						= 0x801E	#   "
	EVENT_MASK					= 0x801F	#   "
	DAMAGED						= 0x8020	# PbufferClobber event_type value
	SAVED						= 0x8021	#   "
	WINDOW						= 0x8022	# PbufferClobber draw_type value
	PBUFFER						= 0x8023	#   "
	PBUFFER_HEIGHT					= 0x8040	# CreateGLXPbuffer attribute
	PBUFFER_WIDTH					= 0x8041	#   "
	VISUAL_CAVEAT_EXT				= 0x20		# Visual attribute
	X_VISUAL_TYPE_EXT				= 0x22		#   "
	TRANSPARENT_TYPE_EXT				= 0x23		#   "
	TRANSPARENT_INDEX_VALUE_EXT			= 0x24		#   "
	TRANSPARENT_RED_VALUE_EXT			= 0x25		#   "
	TRANSPARENT_GREEN_VALUE_EXT			= 0x26		#   "
	TRANSPARENT_BLUE_VALUE_EXT			= 0x27		#   "
	TRANSPARENT_ALPHA_VALUE_EXT			= 0x28		#   "
	NONE_EXT					= 0x8000	# several EXT attribute values
	SLOW_VISUAL_EXT					= 0x8001	# VISUAL_CAVEAT_EXT attribute value
	TRUE_COLOR_EXT					= 0x8002	# X_VISUAL_TYPE_EXT attribute value
	DIRECT_COLOR_EXT				= 0x8003	#   "
	PSEUDO_COLOR_EXT				= 0x8004	#   "
	STATIC_COLOR_EXT				= 0x8005	#   "
	GRAY_SCALE_EXT					= 0x8006	#   "
	STATIC_GRAY_EXT					= 0x8007	#   "
	TRANSPARENT_RGB_EXT				= 0x8008	# TRANSPARENT_TYPE_EXT attribute value
	TRANSPARENT_INDEX_EXT				= 0x8009	#   "
	SHARE_CONTEXT_EXT				= 0x800A	# QueryContextInfoEXT attribute
	VISUAL_ID_EXT					= 0x800B	#   "
	SCREEN_EXT					= 0x800C	#   "
	NON_CONFORMANT_VISUAL_EXT			= 0x800D	# VISUAL_CAVEAT_EXT attribute value
	DRAWABLE_TYPE_SGIX				= 0x8010	# FBConfigSGIX attribute
	RENDER_TYPE_SGIX				= 0x8011	#   "
	X_RENDERABLE_SGIX				= 0x8012	#   "
	FBCONFIG_ID_SGIX				= 0x8013	#   "
	RGBA_TYPE_SGIX					= 0x8014	# CreateContextWithConfigSGIX render_type value
	COLOR_INDEX_TYPE_SGIX				= 0x8015	#   "
	MAX_PBUFFER_WIDTH_SGIX				= 0x8016	# FBConfigSGIX attribute
	MAX_PBUFFER_HEIGHT_SGIX				= 0x8017	#   "
	MAX_PBUFFER_PIXELS_SGIX				= 0x8018	#   "
	OPTIMAL_PBUFFER_WIDTH_SGIX			= 0x8019	#   "
	OPTIMAL_PBUFFER_HEIGHT_SGIX			= 0x801A	#   "
	PRESERVED_CONTENTS_SGIX				= 0x801B	# PbufferSGIX attribute
	LARGEST_PBUFFER_SGIX				= 0x801C	#   "
	WIDTH_SGIX					= 0x801D	#   "
	HEIGHT_SGIX					= 0x801E	#   "
	EVENT_MASK_SGIX					= 0x801F	#   "
	DAMAGED_SGIX					= 0x8020	# BufferClobberSGIX event_type value
	SAVED_SGIX					= 0x8021	#   "
	WINDOW_SGIX					= 0x8022	# BufferClobberSGIX draw_type value
	PBUFFER_SGIX					= 0x8023	#   "
	DIGITAL_MEDIA_PBUFFER_SGIX			= 0x8024	# PbufferSGIX attribute
	BLENDED_RGBA_SGIS				= 0x8025	# TRANSPARENT_TYPE_EXT attribute value
	MULTISAMPLE_SUB_RECT_WIDTH_SGIS			= 0x8026	# Visual attribute (shared_multisample)
	MULTISAMPLE_SUB_RECT_HEIGHT_SGIS		= 0x8027	#   "
	SAMPLE_BUFFERS_SGIS				= 100000	# Visual attribute (multisample)
	SAMPLES_SGIS					= 100001	#   "

###############################################################################

# SGI_future_use: 0x8028-0x803F

###############################################################################

# ARB_future_use: 0x8042-0x804F

###############################################################################

# 3DFX: 0x8050-0x805F

# 3DFX_multisample enum:
#	SAMPLE_BUFFERS_3DFX				= 0x8050
#	SAMPLES_3DFX					= 0x8051

###############################################################################

###############################################################################
### PLEASE REMEMBER THAT NEW ENUMERANT ALLOCATIONS MUST BE OBTAINED BY
### REQUEST TO SGI'S ARB REPRESENTATIVE (see comments at the top of this file)
###############################################################################

# Any_vendor_future_use: 0x8060-0xFFFF
#
#   This range must be the last range in the file.  To generate a new
#   range, allocate multiples of 16 from the beginning of the
#   Any_vendor_future_use range and update enum.spec
