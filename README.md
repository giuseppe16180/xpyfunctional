# xPyFunctional
This repository contains all the extensions i needed for the library PyFunctional.

To use the extensions, import simply import this module as follow:

```python
from xfunctional import unpack as u
from functional import seq as s

(
    s([['key1', [1, 2, 3]], ['key2', [4, 5, 6]]])
    .expand_with_key() # type: ignore
    .flip() # type: ignore
    .map(u(lambda k, v: (k, v)))
    .to_list()
)
```

Outputs: `[(1, 'key1'), (2, 'key1'), (3, 'key1'), (4, 'key2'), (5, 'key2'), (6, 'key2')]`

The following functions are available:

+ `expand_with_key`
+ `flip`

In addition the `unpack` function allows you to give different names to all the different parameters of the lambda and avoiding to give a single tuple as parameter where the specific elements are accessed in a positional fashion.
