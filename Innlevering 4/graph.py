from collections import defaultdict
from itertools import combinations
import graphviz
from collections import deque
from heapq import heappush, heappop
import math

def main():
    g = build_graph("input/movies.tsv", "input/actors.tsv")


def build_graph(file_movies, file_actors):
    G = Graph()
    movies = read_movies(file_movies)
    read_actors(G, movies, file_actors)
    for movie in movies:
        m = movies[movie]
        actor_list = list(m.actors)
        for v, u in combinations(actor_list, 2):
            G.addEdge(v, u, m)
    return G


def read_actors(G, movies, file_actors):
        with open(file_actors, "r", encoding="utf8") as file:
            for line in file:
                a = line.rstrip().split("\t")
                actor = Actor(a[0], a[1], a[2:])
                G.addVertex(actor)
                for movie in actor.movies:
                    if movie in movies:
                        movies[movie].actors.add(actor)
        

class Graph:
    def __init__(self):
        self.V = set()
        self.E = defaultdict(set)
        self.W = defaultdict(set)
        self.len_E = 0

    def addVertex(self, v):
        self.V.add(v)

    def addEdge(self, v, u, w):
        if u != v:
            self.E[v].add(u)
            self.E[u].add(v)
            self.W[(u, v)].add(w)
            self.W[(v, u)].add(w)
            self.len_E += 1

    def get_highest_rated(self, v, u):
        movies = self.W[(v, u)]
        high = 0
        mov = None
        for movie in movies:
            if movie.rating > high:
                high = movie.rating
                mov = movie
        return mov

    def getLenE(self):
        return self.len_E


def read_movies(filename):
    movies = {}
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            m = line.rstrip().split("\t")
            movie = Movie(m[0], m[1], m[2], m[3])
            movies[movie.id] = movie
    return movies


class Actor:
    def __init__(self, id, name, movies):
        self.id = id
        self.name = name
        self.movies = movies

    def __repr__(self):
        return f"{self.name}"
    
    def __lt__(self, other):
        return self.id < other.id
    

class Movie:
    def __init__(self, id, title, rating, votes):
        self.id = id
        self.title = title
        self.rating = float(rating)
        self.votes = int(votes)
        self.actors = set()

    def __repr__(self):
        return str(self.title)


def drawgraph(G):
    dot = graphviz.Graph()
    seen_edges = set()
    for u in G.V:
        dot.node(u.name)
        for v in G.E[u]:
            if (v, u) in seen_edges:
                continue
            seen_edges.add((u, v))
            dot.edge(u.name, v.name, label=str(G.W[(u, v)]))
    dot.render('graph', format='svg')