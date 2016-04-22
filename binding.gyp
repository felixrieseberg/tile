{
    'targets': [{
        'target_name': 'tile',
        'include_dirs': ['<!(node -e "require(\'nan\')")'],
        'sources': [
            'src/main.cc',
            'src/tile.h',
        ],
        'conditions': [
            ['OS=="win"', {
                'sources': [
                    'src/tile_win.cc',
                ],
                'msvs_settings': {
                    'VCCLCompilerTool': {
                        'RuntimeLibrary': 'MultiThreadedDebug',
                        'ExceptionHandling': '0',
                        'AdditionalOptions': [
                            '/MDd',
                            '/ZW'
                        ],
                        'AdditionalIncludeDirectories': [
                            'C:\Program Files (x86)\Microsoft Visual Studio 15.0\VC\vcpackages'
                        ]
                    },
                }
            }]
        ],
    }]
}