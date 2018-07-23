from graphviz import Digraph

def graphviz_visualization(net):
    viz = Digraph(net.name, filename=net.name+'.gv', engine='dot')

    #transitions
    viz.attr('node', shape='box')
    for t in net.transitions:
        viz.node(t.name, t.label)

    #places
    viz.attr('node', shape='circle', fixedsize='true', width='0.75')
    for p in net.places:
        viz.node(p.name)

    #arcs
    for a in net.arcs:
        viz.edge(a.source.name, a.target.name)

    viz.attr(overlap='false')
    viz.attr(fontsize='11')

    return viz

