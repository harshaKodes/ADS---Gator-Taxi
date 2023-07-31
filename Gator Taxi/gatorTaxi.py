import sys

from model_gatorride import RideGatorTaxi
from heap_minimum import HeapMinimum
from heap_minimum import LowestHeapNode
from red_nblack_tree import RedNBlackTree, RedNBlackTreeNode


def gatorride_insertion(gatorride, data_heap, rednblacktree):
    if rednblacktree.get_gatorride(gatorride.rideNumber) is not None:
        output_update(None, "Duplicate RideNumber", False)
        sys.exit(0)
        return
    rednblacktree_node = RedNBlackTreeNode(None, None)
    minimum_heap_node = LowestHeapNode(gatorride, rednblacktree_node, data_heap.size_present + 1)
    data_heap.insert(minimum_heap_node)
    rednblacktree.insert(gatorride, minimum_heap_node)


def output_update(gatorride, string_message, list_gatorrides):
    file = open("output_file.txt", "a")
    if gatorride is None:
        file.write(string_message + "\n")
    else:
        string_message = ""
        if not list_gatorrides:
            string_message += ("(" + str(gatorride.rideNumber) + "," + str(gatorride.rideCost) + "," + str(gatorride.tripDuration) + ")\n")
        else:
            if len(gatorride) == 0:
                string_message += "(0,0,0)\n"
            for i in range(len(gatorride)):
                if i != len(gatorride) - 1:
                    string_message = string_message + ("(" + str(gatorride[i].rideNumber) + "," + str(gatorride[i].rideCost) + "," + str(
                        gatorride[i].tripDuration) + "),")
                else:
                    string_message = string_message + ("(" + str(gatorride[i].rideNumber) + "," + str(gatorride[i].rideCost) + "," + str(
                        gatorride[i].tripDuration) + ")\n")

        file.write(string_message)
    file.close()


def list_gatorrides(rideNumber, rednblacktree):
    gatortaxi_result = rednblacktree.get_gatorride(rideNumber)
    if gatortaxi_result is None:
        output_update(RideGatorTaxi(0, 0, 0), "", False)
    else:
        output_update(gatortaxi_result.gatorride, "", False)


def gatorride_rangeoutput(begin, end, rednblacktree):
    list_gatorrides = rednblacktree.get_gatorrides_in_range(begin, end)
    output_update(list_gatorrides, "", True)


def request_next_gatorride(data_heap, rednblacktree):
    if data_heap.size_present != 0:
        popped_node = data_heap.pop()
        rednblacktree.gatortaxi_node_deletion(popped_node.gatorride.rideNumber)
        output_update(popped_node.gatorride, "", False)
    else:
        output_update(None, "No active ride requests", False)


def calloff_gatorride(ride_number, data_heap, rednblacktree):
    heap_node = rednblacktree.gatortaxi_node_deletion(ride_number)
    if heap_node is not None:
        data_heap.heap_element_deletion(heap_node.heap_index_lowest)


def gatorride_updation(rideNumber, new_duration, data_heap, rednblacktree):
    rednblacktree_node = rednblacktree.get_gatorride(rideNumber)
    if rednblacktree_node is None:
        print("")
        # output_update(None, "No ride found to update", False)
    elif new_duration <= rednblacktree_node.gatorride.tripDuration:
        data_heap.heap_element_updation(rednblacktree_node.minimum_heap_node.heap_index_lowest, new_duration)
    elif rednblacktree_node.gatorride.tripDuration < new_duration <= (2 * rednblacktree_node.gatorride.tripDuration):
        calloff_gatorride(rednblacktree_node.gatorride.rideNumber, data_heap, rednblacktree)
        gatorride_insertion(RideGatorTaxi(rednblacktree_node.gatorride.rideNumber, rednblacktree_node.gatorride.rideCost + 10, new_duration), data_heap, rednblacktree)
    else:
        calloff_gatorride(rednblacktree_node.gatorride.rideNumber, data_heap, rednblacktree)


if __name__ == "__main__":
    data_heap = HeapMinimum()
    rednblacktree = RedNBlackTree()
    input_file = sys.argv[1]
    file = open("output_file.txt", "w")
    file.close()
    file = open(input_file, "r")
    for s in file.readlines():
        n = []
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
        if "Insert" in s:
            gatorride_insertion(RideGatorTaxi(n[0], n[1], n[2]), data_heap, rednblacktree)
        elif "Print" in s:
            if len(n) == 1:
                list_gatorrides(n[0], rednblacktree)
            elif len(n) == 2:
                gatorride_rangeoutput(n[0], n[1], rednblacktree)
        elif "UpdateTrip" in s:
            gatorride_updation(n[0], n[1], data_heap, rednblacktree)
        elif "GetNextRide" in s:
            request_next_gatorride(data_heap, rednblacktree)
        elif "CancelRide" in s:
            calloff_gatorride(n[0], data_heap, rednblacktree)

