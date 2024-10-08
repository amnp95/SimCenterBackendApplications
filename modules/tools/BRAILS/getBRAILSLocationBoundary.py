#  # noqa: INP001, D100
# Copyright (c) 2024 The Regents of the University of California
#
# This file is a part of SimCenter backend applications.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# You should have received a copy of the BSD 3-Clause License along with
# BRAILS. If not, see <http://www.opensource.org/licenses/>.
#
# Contributors:
# Barbaros Cetiner
#
# Last updated:
# 03-27-2024

# Import packages required for running the latest version of BRAILS:
import argparse
import os
import sys
from time import gmtime, strftime

from brails.workflow.FootprintHandler import FootprintHandler


# Define a standard way of printing program outputs:
def log_msg(msg):  # noqa: D103
    formatted_msg = '{} {}'.format(strftime('%Y-%m-%dT%H:%M:%SZ', gmtime()), msg)
    print(formatted_msg)  # noqa: T201


# Define a way to call BRAILS FootprintHandler:
def runBrails(latMin, latMax, longMin, longMax, locationStr, outputfile):  # noqa: N802, N803, D103
    # Initialize FootprintHandler:
    fpHandler = FootprintHandler()  # noqa: N806
    if locationStr == '""':
        locationStr = ''  # noqa: N806
    # Run FootprintHandler to generate the boundary GeoJSON file for the entered location:
    if locationStr == '':
        fpHandler._FootprintHandler__bbox2poly(  # noqa: SLF001
            (longMin, latMin, longMax, latMax), outfile=outputfile
        )
    else:
        fpHandler._FootprintHandler__fetch_roi(locationStr, outfile=outputfile)  # noqa: SLF001


# Define a way to collect GUI input:
def main(args):  # noqa: D103
    parser = argparse.ArgumentParser()
    parser.add_argument('--latMin', default=None, type=float)
    parser.add_argument('--latMax', default=None, type=float)
    parser.add_argument('--longMin', default=None, type=float)
    parser.add_argument('--longMax', default=None, type=float)
    parser.add_argument('--location', default=None, type=str)
    parser.add_argument('--outputFile', default=None)

    args = parser.parse_args(args)

    # Create the folder for the user-defined output directory, if it does not exist:
    outdir = os.path.abspath(args.outputFile).replace(  # noqa: PTH100
        os.path.split(args.outputFile)[-1], ''
    )
    os.makedirs(outdir, exist_ok=True)  # noqa: PTH103

    # Run BRAILS FootprintHandler with the user-defined arguments:
    runBrails(
        args.latMin,
        args.latMax,
        args.longMin,
        args.longMax,
        args.location,
        args.outputFile,
    )

    log_msg('BRAILS successfully generated the requested boundary polygon')


# Run main:
if __name__ == '__main__':
    main(sys.argv[1:])
