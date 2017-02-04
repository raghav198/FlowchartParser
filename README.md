# Flowchart Parser
## Description
The aim of FlowchartParser is to analyze simple programs and convert them into flowcharts for easier visualization. It functions as a command line tool consisting of 4 python scripts, including an analyzer as well as a (work in progress) visualizer.

## Usage
There are 4 `.py` files that come with FlowchartParser, `flowchart.py` (the parser), `display.py` (the visualizer), and `regexes.py` and `node.py` (library files). `flowchart.py` is the main analysis script. Usage for `flowchart.py` is as follows:

    python3 flowchart.py my_script.py output_file.flow
	
The parser will analyze the contents of `my_script.py` and attempt to generate a flowchart, the data for which will be stored in `output_file.flow`. Note that the contents of `output_file.flow` are serialized; that is, the file is a binary and is not meant to be read by a machine, not a human. There is a second `display.py` script that can be used for this purpose. Usage for `display.py` is as follows:

    python3 display.py output_file.flow
	
The visualizer will read the contents of `output_file.flow` and reconstruct the flowchart, and then display a visualization.

## Further Development
FlowchartParser is currently an alpha release. This means that there are likely many bugs; if you notice one, please submit an issue to this repository with a replicable level of detail. The following are some features to look for in future releases:

  * Support for syntax other than python
  * A graphics frontend for the visualizer instead of a text-based walkthrough

