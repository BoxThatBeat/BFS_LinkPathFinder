import argparse
from queue import Queue

from DynamicTree import DynamicTree
from SteamTree import SteamTree
from TestTree import TestTree


def arg_setup():

    parser = argparse.ArgumentParser(description="A program that takes a Facebook profile source and goal and determines the shortest link clicks to get from source to goal through friend lists.")
    parser.add_argument("source_profile", metavar="source_profile", type=str, help="The source Facebook profile URL")
    parser.add_argument("target_profile", metavar="target_profile", type=str, help="The target Facebook profile URL")
    return parser.parse_args()

def create_path_to_goal(super_map, root, target) -> list:
    """
    Uses the supermap which has enteries of subnode to it's super node to create the path from root to target node
    returns such path as a list
    """

    path = [target]
    while path[-1] != root:
        path.append(super_map[path[-1]])
    path.reverse()
    return path

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

        print(node)
        if node == target_node:
            return create_path_to_goal(super_map, root_node, target_node)

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
    print(f"Target is {len(path_to_target)} friends away from source profile. With friend path of:")
    print(path_to_target)


def main():
    print("Running Link Path Finder")
    

    args = arg_setup()
    find_path(SteamTree(args.source_profile), args.target_profile)
    #find_path(TestTree('root'), 'F1')



if __name__ == "__main__":
    main()
