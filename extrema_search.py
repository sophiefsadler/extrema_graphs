#!/usr/bin/env python
# coding: utf-8
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy import optimize
from matplotlib import cm
import matplotlib.pyplot as plt
import random
import networkx as nx
from scipy.spatial import distance
from scipy import interpolate
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import norm
from pynmmso import Nmmso
plt.rcParams.update({
    # "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Computer Modern Serif"],
    "font.size":24})
plt.ion()

def get_points(n_dim, n_samples=100, centre=np.zeros(2), radius=1):
    return np.array([get_point(n_dim) for i in range(n_samples)]) * radius + centre

def get_point(n_dim):
    x = np.zeros(n_dim)
    for i in range(n_dim):
        x[i] = norm.rvs()
    return (1/np.sqrt(np.sum(x**2))) * x


def intermediate_points_vectorised(p1, p2, nb_points=50):
    weights = np.linspace(0, 1, nb_points)[1:-1]
    return [i*p1 + (1-i)*p2 for i in weights]

def extrema_search(funMax, funMin, number_of_fitness_evaluations=10000, radius_percentage=0.05,
                    do_plot=True, nb_points=5, do_scaling=False, do_sphere=False, nsph_points=100, 
                   keep_percentage=0.9, seed=121283516, nmds=True, plot_save=True, plot_save_name=None):
    np.random.seed(seed)
    lb, ub = np.array(funMax.get_bounds())
    radius = radius_percentage * distance.euclidean(ub ,lb)
    func_values_matching_optima = []
    print("Looking for maxima...")
    maxs_found = []
    nmmso = Nmmso(funMax())
    my_result = nmmso.run(number_of_fitness_evaluations)
    for mode_result in my_result:
        maxs_found.append(mode_result.location)
        func_values_matching_optima.append(mode_result.value)
    print("Done.")
    print("Looking for minima...")
    mins_found = []
    nmmso = Nmmso(funMin())
    my_result = nmmso.run(number_of_fitness_evaluations)
    for mode_result in my_result:
        mins_found.append(mode_result.location)
        func_values_matching_optima.append(-mode_result.value)
    optima = np.stack(mins_found + maxs_found, axis=0)
    print("Done.")
    print("Augmenting data with edge nodes...")
    edges = []
    for i in range(len(optima)):
        for j in range(len(optima)):
            if i != j:
                dist = distance.euclidean(optima[i, :], optima[j, :])
                if dist < radius:  ## Distance chosen arbitrarily
                    if (min(i,j), max(i,j)) not in edges:
                        edges.append((i,j))

    new_data = []
    for i in range(len(optima)):
        new_data.append(optima[i,:])
    for edge in edges:
        pos_node_1 = optima[edge[0], :]
        pos_node_2 = optima[edge[1], :]
        new_nodes = intermediate_points_vectorised(pos_node_1, pos_node_2, nb_points=nb_points)
        for node in new_nodes:
            new_data.append(np.array(node))
    data_length = len(new_data)
    # add a sphere
    if do_sphere:
        random_opt = np.random.choice(range(len(optima)))
        sphere_pts = get_points(len(lb), n_samples=nsph_points, centre=optima[random_opt], radius=radius)
        new_data = np.concatenate([np.array(new_data), sphere_pts])
    else:
        new_data = np.array(new_data)
    print("Total number of optima: ", len(optima))
    print("Total number of points:", len(new_data))
    print("Done.")
    print("Scaling data...")
    if do_scaling:
        scaler = MinMaxScaler()
        new_data_scaled = scaler.fit_transform(new_data)
    else:
        new_data_scaled = new_data
    print("Done.")
    print("Perform MDS...")
    mds = MDS(2, random_state=0, metric=nmds)
    mds_new_data = mds.fit_transform(new_data_scaled)
    print("Done.")
    # exclude some points from graph
    if do_sphere:
        dists = []
        for i in mds_new_data[-nsph_points:]:
            dist = distance.euclidean(mds_new_data[random_opt], i)
            dists.append(dist)
        mx_dist =  np.max(dists)
        inds = np.where(dists <= keep_percentage * mx_dist)[0] + data_length
        new_data = np.delete(new_data, inds, 0)
        mds_new_data = np.delete(mds_new_data, inds, 0)        
    G = nx.Graph()
    G.add_nodes_from([i for i in range(len(new_data))])

    x = mds_new_data[:, 0]
    y = mds_new_data[:, 1]

    if do_plot:
        pos = {i: [x[i], y[i]] for i in range(len(new_data))}
        plt.rcParams['figure.figsize'] = [25, 15]
        node_sizes = [500 for _ in range(len(optima))] + [50 for _ in range(G.number_of_nodes() - len(optima))]
        func_val_map = {i: funMax.fitness(new_data[i]) for i in range(len(new_data))}
        values = [func_val_map[node] for node in G.nodes()]
        fig, ax = plt.subplots()
        nodes = nx.draw(G, pos=pos, ax=ax, node_size=node_sizes, node_color=values)
        # ax= plt.gca()
        ax.collections[0].set_edgecolor("#000000")
        limits=plt.axis('on')
        sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin = np.min(values), vmax=np.max(values)))
        sm._A = []
        cbar = plt.colorbar(sm)
        cbar.set_label("Fitness")
        if plot_save:
            plt.savefig(plot_save_name)
    return mds_new_data
