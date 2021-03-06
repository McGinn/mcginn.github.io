# mcginn.github.io [![1]][2] <img align="right" width=76 src="content/images/icons/apple-touch-icon-152x152.png?raw=true"/>

This repository contains both the static site files and the source files used
to generate **[blog.alexandermcginn.com]**. The website is generated with [Pelican] using a
custom theme: [Pneumatic]. The styling and implementation are based entirely on [kevinyap.ca]. In order to host with [GitHub Pages], the repository
contains two distinct branches; the [`src`] branch contains the source files
that Pelican uses to generate the static files which are automatically
[pushed][generate.sh] to the [`master`] branch by Travis CI (see
[this blog post][travis-article] for more information on the process).

Code is licensed under the [MIT License], and articles under a [Creative
Commons Attribution License].

[1]: https://api.travis-ci.org/McGinn/mcginn.github.io.svg?branch=src "Build Status"
[2]: https://travis-ci.org/McGinn/mcginn.github.io

[blog.alexandermcginn.com]: http://blog.alexandermcginn.com
[Pelican]: http://getpelican.com
[Pneumatic]: https://github.com/iKevinY/pneumatic
[`src`]: https://github.com/McGinn/mcginn.github.io/tree/src
[`master`]: https://github.com/McGinn/mcginn.github.io/tree/master
[GitHub Pages]: http://pages.github.com
[generate.sh]: generate.sh#L66
[travis-article]: http://kevinyap.ca/2014/06/deploying-pelican-sites-using-travis-ci/
[MIT License]: LICENSE
[Creative Commons Attribution License]: http://creativecommons.org/licenses/by/4.0/
[kevinyap.ca]: http://kevinyap.ca
