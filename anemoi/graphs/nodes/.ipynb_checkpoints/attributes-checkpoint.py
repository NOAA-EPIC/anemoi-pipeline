from __future__ import annotations

import logging
from abc import ABC
from abc import abstractmethod

import numpy as np
import torch
from scipy.spatial import SphericalVoronoi
from torch_geometric.data import HeteroData
from torch_geometric.data.storage import NodeStorage

from anemoi.graphs.generate.transforms import latlon_rad_to_cartesian
from anemoi.graphs.normalizer import NormalizerMixin

LOGGER = logging.getLogger(__name__)


class BaseWeights(ABC, NormalizerMixin):
    """Base class for the weights of the nodes."""

    def __init__(self, norm: str | None = None) -> None:
        self.norm = norm

    @abstractmethod
    def get_raw_values(self, nodes: NodeStorage, *args, **kwargs): ...

#     def get_raw_values(self, nodes: NodeStorage, *args, **kwargs) -> np.ndarray:
#         """Compute the weights.

#         Parameters
#         ----------
#         nodes : NodeStorage
#             Nodes of the graph.
#         args : tuple
#             Additional arguments.
#         kwargs : dict
#             Additional keyword arguments.

#         Returns
#         -------
#         np.ndarray
#             Weights.
#         """
#         return np.ones(nodes.num_nodes)

    def post_process(self, values: np.ndarray) -> torch.Tensor:
        """Post-process the values."""
        if values.ndim == 1:
            values = values[:, np.newaxis]

        norm_values = self.normalize(values)

        return torch.tensor(norm_values, dtype=torch.float32)

    def compute(self, graph: HeteroData, nodes_name: str, *args, **kwargs) -> torch.Tensor:
        """Get the node weights.

        Parameters
        ----------
        graph : HeteroData
            Graph.
        nodes_name : str
            Name of the nodes.
        args : tuple
            Additional arguments.
        kwargs : dict
            Additional keyword arguments.

        Returns
        -------
        torch.Tensor
            Weights associated to the nodes.
        """
        nodes = graph[nodes_name]
        print("***graphs", graph)
        print("\nnodes_name", nodes_name)
        print("@@** NODES***",nodes)
        print("^^SELF.NORM", self.norm)

        weights =  self.get_raw_values(nodes, *args, **kwargs)
        #weights =  BaseWeights(self.norm).get_raw_values(nodes, *args, **kwargs)
        print("**WEIGHTS", weights)
        return self.post_process(weights)


class UniformWeights(BaseWeights):
    """Implements a uniform weight for the nodes.

    Methods
    -------
    compute(self, graph, nodes_name)
        Compute the area attributes for each node.
    """

    def get_raw_values(self, nodes: NodeStorage, *args, **kwargs) -> np.ndarray:
        """Compute the weights.

        Parameters
        ----------
        nodes : NodeStorage
            Nodes of the graph.
        args : tuple
            Additional arguments.
        kwargs : dict
            Additional keyword arguments.

        Returns
        -------
        np.ndarray
            Weights.
        """
        return np.ones(nodes.num_nodes)


class AreaWeights(BaseWeights):
    """Implements the area of the nodes as the weights.

    Attributes
    ----------
    norm : str
        Normalization of the weights.
    radius : float
        Radius of the sphere.
    centre : np.ndarray
        Centre of the sphere.

    Methods
    -------
    compute(self, graph, nodes_name)
        Compute the area attributes for each node.
        
    self.norm='l1' #l1, l2, unit-max, unit-sum, unit-std
    """

    def __init__(self, norm: str | None = None, radius: float = 1.0, centre: np.ndarray = np.array([0, 0, 0])) -> None:
        super().__init__(norm)
        self.radius = radius
        self.centre = centre
        self.norm='unit-sum' 

    def get_raw_values(self, nodes: NodeStorage, *args, **kwargs) -> np.ndarray:
        """Compute the area associated to each node.

        It uses Voronoi diagrams to compute the area of each node.

        Parameters
        ----------
        nodes : NodeStorage
            Nodes of the graph.
        args : tuple
            Additional arguments.
        kwargs : dict
            Additional keyword arguments.

        Returns
        -------
        np.ndarray
            Weights.
        """
        latitudes, longitudes = nodes.x[:, 0], nodes.x[:, 1]
        points = latlon_rad_to_cartesian((np.asarray(latitudes), np.asarray(longitudes)))
# <++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ SC
        # Save the array to a pickle file
        import pickle
        with open('/pscratch/sd/s/schin/pipeline/anemoi-pipeline/nodes.pkl', 'wb') as f:
            pickle.dump(nodes, f)
        with open('/pscratch/sd/s/schin/pipeline/anemoi-pipeline/latitudes.pkl', 'wb') as f:
            pickle.dump(latitudes, f)
        with open('/pscratch/sd/s/schin/pipeline/anemoi-pipeline/longitudes.pkl', 'wb') as f:
            pickle.dump(longitudes, f)
        with open('/pscratch/sd/s/schin/pipeline/anemoi-pipeline/points.pkl', 'wb') as f:
            pickle.dump(points, f)
        print("*self.radius", self.radius)
        print("*self.centre", self.centre)
        #print("*B", points)
        #points= np.unique(points, axis=1)
        #print("*A", points)
        sv = SphericalVoronoi(points, 
                              self.radius,
                              self.centre,
                              threshold=1e-06)
        area_weights = sv.calculate_areas()
        LOGGER.debug(
            "There are %d of weights, which (unscaled) add up a total weight of %.2f.",
            len(area_weights),
            np.array(area_weights).sum(),
        )
        return area_weights
