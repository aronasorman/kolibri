# Imported during settings import, so make sure we don't import any kolibri modules here.

import pkgutil


def find_external_plugins():

    # Find all `kolibri_plugin` modules.
    kolibri_modules = (modname for _, modname, _ in pkgutil.walk_packages(onerror=lambda n: None) if modname.endswith('.kolibri_plugin'))

    for modname in kolibri_modules:

        # remove `.kolibri_plugin` from the module name, to get the package itself.
        # e.g. kolibri_exercise_perseus_renderer.kolibri_plugin -> kolibri_exercise_perseus_renderer
        package, _kolibri_plugin_ext = modname.split('.kolibri_plugin', 1)

        # remove kolibri.dist from the module name, to get the true package name
        # too. helpful when we're importing from inside the kolibri environment,
        # where kolibri/dist is prepended to the path.
        # e.g. kolibri.dist.exercise_perseus_rendere -> exercise_perseus_renderer
        try:
            _kolibri_dist_prefix, package = package.split('kolibri.dist.', 1)
        except ValueError:  # the modules doesn't have the kolibri.dist prefix. Skip.
            pass

        yield package
