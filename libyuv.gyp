# Copyright (c) 2011 The LibYuv project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'targets': [
    {
      'target_name': 'libyuv',
      'type': 'static_library',
      'include_dirs': [
        'common',
        'include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'common',
          'include',
        ],
      },
      'sources': [
        # includes
        'include/convert.h',
        'include/general.h',
        'include/scale.h',
        'include/planar_functions.h',

        # headers
        'common/basic_types.h',
        'common/common.h',
        'common/constructor_magic.h',
        'source/cpu_id.h',
        'source/row.h',
        'source/video_common.h',

        # sources
        'source/convert.cc',
        'source/cpu_id.cc',
        'source/format_conversion.cc',
        'source/general.cc',
        'source/planar_functions.cc',
        'source/row_posix.cc',
        'source/row_table.cc',
        'source/scale.cc',
        'source/video_common.cc',
      ],
    },
  ], # targets
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
