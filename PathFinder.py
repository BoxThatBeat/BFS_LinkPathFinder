import argparse
from queue import Queue

from DynamicTree import DynamicTree
from SteamApiTree import SteamApiTree
from SteamWebTree import SteamWebTree
from TestTree import TestTree
import time


def arg_setup():

    parser = argparse.ArgumentParser(description="A program that takes a Facebook profile source and goal and determines the shortest link clicks to get from source to goal through friend lists.")
    parser.add_argument("source_profile", metavar="source_profile", type=str, help="The source Steam profile URL or steam_id in the case of providing a Steam API key")
    parser.add_argument("target_profile", metavar="target_profile", type=str, help="The target Steam profile URL or steam_id in the case of providing a Steam API key")
    parser.add_argument("-api_key", metavar="api_key", type=str, help="An optional Steam api key that will enable the use of Steam's API for faster run time.")
    return parser.parse_args()

def create_path_to_goal(dynamic_tree: DynamicTree, super_map, root, target) -> list:
    """
    Uses the supermap which has enteries of subnode to it's super node to create the path from root to target node
    returns such path as a list
    """

    path = [target]
    while path[-1] != root:
        path.append(super_map[path[-1]])
    path.reverse()

    return dynamic_tree.format_output(path)

def breadth_first_search(dynamic_tree: DynamicTree, target_node) -> list:
    """
    Returns the shortest path between the root node of the tree and the target_node as an ordered list
    """

    root_node = dynamic_tree.get_root()

    visited = {root_node}
    search_queue = Queue(maxsize=-1)
    search_queue.put(root_node)
    super_map = {}
    
    while search_queue:
        node = search_queue.get()

        #print(node)
        if node == target_node:
            return create_path_to_goal(dynamic_tree, super_map, root_node, target_node)

        for sub_node in dynamic_tree.get_sub_nodes(node):
            if not sub_node in visited:
                #add all sub nodes of the current node to the queue, behind all other nodes in the queue
                search_queue.put(sub_node)

                #add sub nodes to supermap and mark as visited
                visited.add(sub_node)
                super_map[sub_node] = node

    return []
                


def find_path(dynamic_tree: DynamicTree, target_node):

    print(f"Begining search for {target_node}")
    path_to_target = breadth_first_search(dynamic_tree, target_node)

    print("Search complete")
    print(f"Target is {len(path_to_target) - 1} friends away from source profile. With friend path of:")
    print(path_to_target)


def main():
    print("Running Link Path Finder")
    
    
    args = arg_setup()

    if args.api_key:
        print("Finding friend path using api:")
        start = time.time()
        find_path(SteamApiTree(args.source_profile, args.api_key), args.target_profile)
        end = time.time()
        print(f"Search took {end - start} seconds.")
    
    else:
        print("Finding friend path using web scraping:")
        start = time.time()
        find_path(SteamWebTree(args.source_profile), args.target_profile)
        end = time.time()
        print(f"Search took {end - start} seconds.")

    #find_path(TestTree("root"), "F2")



if __name__ == "__main__":
    main()
