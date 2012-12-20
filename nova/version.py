# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright 2011 OpenStack LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

NOVA_VENDOR = "OpenStack Foundation"
NOVA_PRODUCT = "OpenStack Nova"
NOVA_PACKAGE = None  # OS distro package version suffix
NOVA_VERSION = ['2013', '1', None]
YEAR, COUNT, REVISION = NOVA_VERSION
FINAL = False   # This becomes true at Release Candidate time


def vendor_string():
    return NOVA_VENDOR


def product_string():
    return NOVA_PRODUCT


def package_string():
    return NOVA_PACKAGE


def canonical_version_string():
    return '.'.join(filter(None, NOVA_VERSION))


def version_string():
    if FINAL:
        return canonical_version_string()
    else:
        return '%s-dev' % (canonical_version_string(),)


def version_string_with_package():
    if package_string() is None:
        return canonical_version_string()
    else:
        return "%s-%s" % (canonical_version_string(), package_string())
