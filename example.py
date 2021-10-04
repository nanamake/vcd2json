#!/usr/bin/env python3
"""Examples of using the vcd2json module."""

from vcd2json import WaveExtractor


def example1():
    """Check the path name of the signal in the VCD file."""

    extractor = WaveExtractor('timer.vcd', '', [])
    extractor.print_props()


if __name__ == '__main__':
    print('')
    print('Example 1')
    print('----------------------------------------')
    example1()

    # Example 1
    # ----------------------------------------
    # vcd_file  = 'timer.vcd'
    # json_file = ''
    # path_list = ['tb_timer/clock',
    #              'tb_timer/pulse',
    #              'tb_timer/reset',
    #              'tb_timer/u_timer/clock',
    #              'tb_timer/u_timer/count',
    #              'tb_timer/u_timer/count_eq11',
    #              'tb_timer/u_timer/pulse',
    #              'tb_timer/u_timer/reset']
    # wave_chunk = 20
    # start_time = 0
    # end_time   = 0


def example2():
    """Extract the signal values specified in the path list
       and output WaveJSON string to the file."""

    path_list = ['tb_timer/u_timer/clock',
                 'tb_timer/u_timer/reset',
                 'tb_timer/u_timer/pulse',
                 'tb_timer/u_timer/count_eq11',
                 'tb_timer/u_timer/count']

    extractor = WaveExtractor('timer.vcd', 'timer.json', path_list)
    extractor.execute()


if __name__ == '__main__':
    print('')
    print('')
    print('Example 2')
    print('----------------------------------------')
    example2()

    # Example 2
    # ----------------------------------------
    # vcd_file  = 'timer.vcd'
    # json_file = 'timer.json'
    # path_list = ['tb_timer/u_timer/clock',
    #              'tb_timer/u_timer/reset',
    #              'tb_timer/u_timer/pulse',
    #              'tb_timer/u_timer/count_eq11',
    #              'tb_timer/u_timer/count']
    # wave_chunk = 20
    # start_time = 0
    # end_time   = 0
    #
    # Create WaveJSON file "timer.json".


def example3():
    """Set sampling duration and display format.
       The result is displayed on standard output."""

    path_list = ['tb_timer/u_timer/clock',
                 'tb_timer/u_timer/reset',
                 'tb_timer/u_timer/pulse',
                 'tb_timer/u_timer/count_eq11',
                 'tb_timer/u_timer/count']

    extractor = WaveExtractor('timer.vcd', '', path_list)
    extractor.wave_chunk = 10
    extractor.start_time = 100
    extractor.end_time = 500
    extractor.wave_format('tb_timer/u_timer/count', 'u')
    extractor.execute()


if __name__ == '__main__':
    print('')
    print('')
    print('Example 3')
    print('----------------------------------------')
    example3()

    # Example 3
    # ----------------------------------------
    # { head: {tock:1},
    #   signal: [
    #   {   name: 'clock'     , wave: 'p.........' },
    #   {},
    #   ['110',
    #     { name: 'reset'     , wave: '1...0.....' },
    #     { name: 'pulse'     , wave: 'x0........' },
    #     { name: 'count_eq11', wave: '0.........' },
    #     { name: 'count'     , wave: '=....=====', data: '0 1 2 3 4 5' },
    #   ],
    #   {},
    #   ['310',
    #     { name: 'reset'     , wave: '0.........' },
    #     { name: 'pulse'     , wave: '0.....10..' },
    #     { name: 'count_eq11', wave: '0....10...' },
    #     { name: 'count'     , wave: '==========', data: '6 7 8 9 10 11 0 1 2 3' },
    #   ],
    #   ],
    # }
