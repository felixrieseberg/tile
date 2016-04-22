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
                        'AdditionalOptions': [
                            '/ZW'
                        ]
                    },
                }
            }]
        ],
    }]
}