 awk -F' ' '{print $3}' Sorted_all_blocks_merged_simulated_hopg.txt |sort|uniq -d|grep -F -f - Sorted_all_blocks_merged_simulated_hopg.txt > t
