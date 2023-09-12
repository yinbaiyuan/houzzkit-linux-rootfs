# Copyright © 2011 Raphaël Hertzog <hertzog@debian.org>
# Copyright © 2012 Guillem Jover <guillem@debian.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

package Dpkg::File;

use strict;
use warnings;

our $VERSION = '0.01';
our @EXPORT = qw(
    file_slurp
);

use Exporter qw(import);

sub file_slurp {
    my $fh = shift;

    local $/;
    my $data = <$fh>;
    return $data;
}

1;
