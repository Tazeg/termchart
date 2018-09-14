### TermChart

Draw ascii line charts in terminal.

![termchart_screenshot](https://raw.githubusercontent.com/Tazeg/termchart/master/termchart_screenshot.png)

### Install

```bash
pip3 install termchart
```

### USage

Create a Python file :

```python
import termchart

graph = termchart.Graph([1,2,3,2,5,1,-1,-5,-3])
graph.draw()
```

You can change the plot (default is `+`):

```python
graph.setDot('|')
```

Change the width and height (default cols is 160x50)
```python
graph.setCols(200)
graph.setRows(40)
```

### Donate

<https://en.jeffprod.com/donate/>
