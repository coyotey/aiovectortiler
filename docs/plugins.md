# Plugins

aiovectortiler comes with a very lite plugin system.

A plugin is a python class that implements one or more [hooks](#hooks). Here is
a very basic example:

    class MyPlugin(object):

        def on_request(self, endpoint, request, **kwargs):
            if request.path == 'xxx':
                return some_response

You then need to [register it](#registering-a-plugin).

## Registering a plugin

Just add its path into the `PLUGINS` [config](config.md) key.

    PLUGINS = ['path/to/plugin_file']

## Hooks

### on_before_load(config)

Sent before loading the recipes.

Parameters:

* **config**: the [config](config.md) object

### on_load(config, recipes)

Sent after loading the recipes.

Parameters:

* **config**: the [config](config.md) object
* **recipes**: the loaded recipes

### on_request(request, **kwargs)

Sent on request processing. 
If the hook returns a response, this response will be used and returned without calling the others hooks in the list nor the utilery view.

Parameters:

* **endpoint**: the targeted endpoint (one of `pbf`, `json`, `geojson`, `tilejson`)
* **request**: the processed request. It's a [aiohttp request instance](http://aiohttp.readthedocs.io/en/stable/web_reference.html#request).
* ****kwargs** URL kwargs of the endpoint; for the tile endpoints: `recipe`, `names`, `z`, `x`, `y`.

### on_response(response, request)

Sent on request processing. If the hook returns a response, this response will be used and returned instead of the normal response.

Parameters:

* **response**: the returned response. It's a [aiohttp response instance](http://aiohttp.readthedocs.io/en/stable/web_reference.html#response).
* **request**: the processed request. It's a [aiohttp request instance](http://aiohttp.readthedocs.io/en/stable/web_reference.html#request).
