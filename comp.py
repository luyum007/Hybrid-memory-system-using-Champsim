with open('stats_sram_50M.txt') as f1, open('stats_hybrid_50M.txt') as f2, open('stats_stt_50M.txt') as f3, open('comp_50M.txt', 'w') as fout:
    # Read every alternate line from each file
    for i, (line1, line2, line3) in enumerate(zip(f1, f2, f3)):
        if i % 2 == 1:
            words1 = line1.strip().split()
            words2 = line2.strip().split()
            words3 = line3.strip().split()
            
            # Check if the list has at least one element
            if words1:
                last_word1 = words1[-1]
            else:
                last_word1 = "N/A"  # or any default value you prefer
            
            if words2:
                last_word2 = words2[-1]
            else:
                last_word2 = "N/A"
            
            if words3:
                last_word3 = words3[-1]
            else:
                last_word3 = "N/A"
            
            fout.write(f'{last_word1} {last_word2} {last_word3}\n')
