vcd2json
========

This python module generates WaveJSON text string from VCD file.
WaveJSON string can be converted to image file of timing diagram.


Usage
-----
Here is an example. See also [example.py](example.py).

```python
from vcd2json import WaveExtractor

path_list = ['tb_timer/u_timer/clock',
             'tb_timer/u_timer/reset',
             'tb_timer/u_timer/pulse',
             'tb_timer/u_timer/count_eq11',
             'tb_timer/u_timer/count']

extractor = WaveExtractor('timer.vcd', 'timer.json', path_list)
extractor.execute()
```

The following JSON formatted text is generated.

    { "head": {"tock":1},
      "signal": [
      {   "name": "clock"     , "wave": "p..................." },
      {},
      ["10",
        { "name": "reset"     , "wave": "0...1....0.........." },
        { "name": "pulse"     , "wave": "x.....0............." },
        { "name": "count_eq11", "wave": "x....0.............." },
        { "name": "count"     , "wave": "x....=....==========", "data": "0 1 2 3 4 5 6 7 8 9 a" }
      ],
      {},
      ["410",
        { "name": "reset"     , "wave": "0..................." },
        { "name": "pulse"     , "wave": "010..........10....." },
        { "name": "count_eq11", "wave": "10..........10......" },
        { "name": "count"     , "wave": "====================", "data": "b 0 1 2 3 4 5 6 7 8 9 a b 0 1 2 3 4 5 6" }
      ],
      {},
      ["810",
        { "name": "reset"     , "wave": "0........" },
        { "name": "pulse"     , "wave": "0....10.." },
        { "name": "count_eq11", "wave": "0...10..." },
        { "name": "count"     , "wave": "=========", "data": "7 8 9 a b 0 1 2 3" }
      ]
      ]
    }

## Optional: States:

You can pass a dictionary with the FSM states of given signals and the tool will change the numerical format by the name of the state.
i.e.


```python
from vcd2json import WaveExtractor

path_list = ['tb_timer/u_fsm/clock',
             'tb_timer/u_fsm/reset',
             'tb_timer/u_fsm/state']
states_dict = {
    "tb_timer/u_fsm/state[3:0]": {
        0: "IDLE",
        1: "STATE1",
        2: "STATE2",
        3: "STATE3",
        4: "STATE4",
        5: "STATE5",
        6: "STATE6",
        7: "STATE7",
        8: "STATE8",
        9: "STATE9",
    },
}

extractor = WaveExtractor('PATH_TO_YOUR_VCD.vcd', 'fsm.json', path_list)
extractor.execute()
```

The following JSON formatted text is generated.

```
    { "head": {"tock":1},
      "signal": [
      {   "name": "clock"     , "wave": "p..................." },
      {},
      ["10",
        { "name": "reset"     , "wave": "0...1....0.........." },
        { "name": "pulse"     , "wave": "x.....0............." },
        { "name": "fsm"     , "wave": "x....=....==========", "data": "IDLE STATE1 STATE2 STATE3 STATE4 STATE5 STATER6 STATE7 STATE 8 STATE9" }
      ],
      ]
    }
```

Instead of
```
    { "head": {"tock":1},
      "signal": [
      {   "name": "clock"     , "wave": "p..................." },
      {},
      ["10",
        { "name": "reset"     , "wave": "0...1....0.........." },
        { "name": "pulse"     , "wave": "x.....0............." },
        { "name": "state"     , "wave": "x....=....==========", "data": "0 1 2 3 4 5 6 7 8 9" }
      ],
      ]
    }
```

You can create SVG image from WaveJSON by using JavaScript application WaveDrom.

![timing diagram](timer.png)


Module Detail
-------------

    NAME
        vcd2json - Create WaveJSON text string from VCD file.

    CLASSES
        class WaveExtractor(builtins.object)
         |  Methods defined here:
         |
         |  __init__(self, vcd_file, json_file, path_list)
         |      Extract signal values from VCD file and output in JSON format.
         |      Specify VCD filename, JSON filename, and signal path list.
         |      If <json_file> is an empty string, standard output is used.
         |      Use slashes to separate signal path hierarchies.
         |      The first signal of the list is regarded as clock.
         |      Other signals are sampled on the negative edge of the clock.
         |
         |  print_props(self)
         |      Display the properties. If an empty path list is given to
         |      the constructor, display the list created from the VCD file.
         |
         |  wave_format(self, signal_path, fmt)
         |      Set the display format of the multi-bit signal. <fmt> is
         |      one of the following characters. The default is 'x'.
         |      'b' - Binary.
         |      'd' - Signed decimal.
         |      'u' - Unsigned decimal.
         |      'x' - Hexa-decimal, lowercase is used.
         |      'X' - Hexa-decimal, uppercase is used.
         |
         |  execute(self)
         |      Perform signal sampling and JSON generation.
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |
         |  wave_chunk
         |      Number of wave samples per time group.
         |
         |  start_time
         |      Sampling start time.
         |
         |  end_time
         |      Sampling end time.
