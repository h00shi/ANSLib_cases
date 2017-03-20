#!/bin/bash

## Set the location of the generator executable accordingly.
if [ -z "$1" ]; then
    GENERATOR='/home/hooshi/code/threed_quadrature/generator_opt';
else
    GENERATOR="$1";
fi

## GENERATE ``TET'' MESHES
echo "tet_5"
${GENERATOR} n=6 ctype=0 out=tet_5
echo "tet_10"
${GENERATOR} n=11 ctype=0 out=tet_10
echo "tet_20"
${GENERATOR} n=21 ctype=0 out=tet_20
echo "tet_40"
${GENERATOR} n=41 ctype=0 out=tet_40

## GENERATE ``HEX'' MESHES
echo "hex_5"
${GENERATOR} n=6 ctype=1 out=hex_5
echo "hex_10"
${GENERATOR} n=11 ctype=1 out=hex_10
echo "hex_20"
${GENERATOR} n=21 ctype=1 out=hex_20
echo "hex_40"
${GENERATOR} n=41 ctype=1 out=hex_40

## GENERATE ``PRISM'' MESHES
echo "wedge_5"
${GENERATOR} n=6 ctype=2 out=wedge_5
echo "wedge_10"
${GENERATOR} n=11 ctype=2 out=wedge_10
echo "wedge_20"
${GENERATOR} n=21 ctype=2 out=wedge_20
echo "wedge_40"
${GENERATOR} n=41 ctype=2 out=wedge_40

## GENERATE ``PYRAMID'' MESHES
echo "pyramid_5"
${GENERATOR} n=6 ctype=3 out=pyramid_5
echo "pyramid_10"
${GENERATOR} n=11 ctype=3 out=pyramid_10
echo "pyramid_20"
${GENERATOR} n=21 ctype=3 out=pyramid_20
echo "pyramid_40"
${GENERATOR} n=41 ctype=3 out=pyramid_40









