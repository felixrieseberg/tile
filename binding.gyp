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
                    'VCLinkerTool': {
                      'AdditionalOptions': ['/WINMD']  
                    },
                    'VCCLCompilerTool': {
                        'RuntimeLibrary': 'MultiThreadedDebug',
                        'ExceptionHandling': '0',
                        'AdditionalOptions': [
                            '/MDd',
                            '/ZW',
                            '/AI "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\\vcpackages" /AI "C:\Program Files (x86)\Windows Kits\\10\UnionMetadata"'
                        ]
                    },
                }
            }]
        ],
    }]
}