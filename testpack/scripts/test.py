#!/usr/bin/env python3

import unittest
from testpack_helper_library.unittests.dockertests import Test1and1Common


class Test1and1NginxImage(Test1and1Common):

    # <tests to run>

    def test_joomla_get(self):
        driver = self.getChromeDriver()
        driver.get("http://%s:8080/installation/index.php" % (Test1and1Common.container_ip))
        self.assertTrue(
            driver.title.find('Joomla') > -1,
            msg="Joomla not found in title"
        )
 
    # </tests to run>

if __name__ == '__main__':
    unittest.main(verbosity=1)
