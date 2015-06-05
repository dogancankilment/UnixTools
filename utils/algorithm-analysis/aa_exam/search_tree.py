from ete2 import Tree


def search(node, root):
    if root == node:
        print "aranan deger", root
        return root

    else:

        while root.children == True:
            counter = 1
            control = False
            current_nodes = depth(root, counter)

            for cr_node in range(current_nodes):
                if cr_node == node:
                    print "aranan deger", cr_node
                    control = True
                    return cr_node

            if control == False:
                counter += 1


def depth(root, index):
    current_list = []

    for i in range(0, index+1):
        current_list.append(root.traverse("levelorder"))

    #for cr_node in root.traverse("levelorder"):
    #    current_list.append(cr_node)

    return current_list