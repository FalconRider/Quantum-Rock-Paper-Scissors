# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import networkx for graph tools

# -----------------------------------RPS Final  WORKS 1030 001

import networkx as nx

# Import dwave_networkx for d-wave graph tools/functions
import dwave_networkx as dnx

# Import matplotlib.pyplot to draw graphs on screen
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

# Set the solver we're going to use
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

# Create empty graph
G = nx.Graph()

# Add edges to graph - this also adds the nodes
G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 4)])

# Find the maximum independent set, S
S = dnx.maximum_independent_set(G, sampler=sampler, num_reads=10)

# Print the solution for the user

#print('Maximum independent set size found is', len(S))


zz = S[0]

#print ("value of node ************************************************* ",zz)

if zz == 1:
    print("                  ROCK")
if zz == 2:
    print ("                 PAPER")
if zz == 3: 
    print ("                 SCISSORS")  

print("*************** Hit Again Arrow to Play Again *************************************")


#print(S)



