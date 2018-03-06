# Integrating PlotLy into Django

## Notes

- Updated to use Django 2.0

## Magic:

The magic is here:

Python code returns HTML/Javascript that is rendered in the template:

```python
fig = go.Figure(data=data, layout=layout)
plot_div = plot(fig, output_type='div', include_plotlyjs=False)
return plot_div
```

Template rendering the Plot:

HTML head:
```html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```

Somewhere in the HTML body:
```html
<div class="col-md-12">{{plot|safe}}</div>
```

## TLTR;

Tests using Plot.ly inside Django.

**Testing**

- 1D
- 2D
- 3D
- 1D generated from Ajax (to test plotly speed)
- 1D from CSV files
- Live 2D Plot

## Installation

Requirements are in the requirements.txt file.

Use `virtualenv`:

```bash
virtualenv venv
source venv/bin/activate
pip install -U -r requirements.txt
# Run it
cd site1/
python manage.py  runserver 0.0.0.0:8000
```

# Run it:

```bash
cd site1/
./manage.py makemigrations
./manage.py migrate
./manage.py runserver 0.0.0.0:8000
```

Go to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)


## Code:

The main code is in:
```
site1/app1
```

Views:
```
site1/app1/views.py
```

Code for plots is here:
```
site1/app1/plots.py
```

