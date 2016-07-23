from aiovectortiler.utils import import_by_path

class Plugins(object):

    _registry = []
    _hooks = {}

    @classmethod
    def load(cls, server_configs):
        for path in server_configs['builtin_plugins'] + server_configs['plugins']:
            cls.register_plugin(import_by_path(path)())

    @classmethod
    def register_plugin(cls, plugin):
        cls._registry.append(plugin)
        cls.register_hooks(plugin)

    @classmethod
    def register_hooks(cls, plugin):
        for attr in dir(plugin):
            if attr.startswith('on_'):
                cls.register_hook(attr, plugin)

    @classmethod
    def register_hook(cls, attr, plugin):
        key = attr[3:]
        if key not in cls._hooks:
            cls._hooks[key] = []
        cls._hooks[key].append(getattr(plugin, attr))

    @classmethod
    def hook(cls, signal, *args, **kwargs):
        hooks = cls._hooks.get(signal, [])
        for hook in hooks:
            output = hook(*args, **kwargs)
            if output:
                return output
