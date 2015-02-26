__author__ = 'Michael'

from networkx import *

G = lollipop_graph(4,6)
F = lollipop_graph(2,3)

pathlengths=[]

for n in F.nodes():
    print n

print("source vertex {target:length, }")
for v in G.nodes():
    spl=single_source_shortest_path_length(G,v)
    print('%s %s' % (v,spl))
    for p in spl.values():
        pathlengths.append(p)

print('')
print("average shortest path length %s" % (sum(pathlengths)/len(pathlengths)))

# histogram of path lengths
dist={}
for p in pathlengths:
    if p in dist:
        dist[p]+=1
    else:
        dist[p]=1

print('')
print("length #paths")
verts=dist.keys()
for d in sorted(verts):
    print('%s %d' % (d,dist[d]))

print("radius: %d" % radius(G))
print("diameter: %d" % diameter(G))
print("eccentricity: %s" % eccentricity(G))
print("center: %s" % center(G))
print("periphery: %s" % periphery(G))
print("density: %s" % density(G))