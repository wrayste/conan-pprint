# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class PprintConan(ConanFile):
    name = "pprint"
    version = "0.9.1"
    description = "Pretty Printer for Modern C++"
    # topics can get used for searches, GitHub topics, Bintray tags etc. Add here keywords about the library
    topics = ("conan", "pprint")
    url = "https://github.com/wrayst/conan-pprint"
    homepage = "https://github.com/p-ranav/pprint"
    author = "wrayste"
    license = "MIT"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE"]

    # Custom attributes for Bincrafters recipe conventions
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/p-ranav/pprint"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url,
                                                   self.version), sha256="b9cc0d42f7be4abbb50b2e3b6a89589c5399201a3dc1fd7cfa72d412afdb2f86")
        extracted_dir = self.name + "-" + self.version

        # Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses",
                  src=self._source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
