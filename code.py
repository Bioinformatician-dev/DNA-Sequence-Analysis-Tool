import matplotlib.pyplot as plt
import seaborn as sns

class DNAAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.gc_content = self.calculate_gc_content()
        self.reverse_complement = self.get_reverse_complement()

    def calculate_gc_content(self):
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        total_bases = len(self.sequence)
        return (g_count + c_count) / total_bases * 100 if total_bases > 0 else 0

    def get_reverse_complement(self):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement[base] for base in reversed(self.sequence))

    def search_motif(self, motif):
        return [i for i in range(len(self.sequence)) if self.sequence.startswith(motif, i)]

    def visualize_sequence(self):
        base_counts = {base: self.sequence.count(base) for base in 'ATCG'}
        sns.barplot(x=list(base_counts.keys()), y=list(base_counts.values()))
        plt.title('Base Composition of DNA Sequence')
        plt.xlabel('Nucleotide')
        plt.ylabel('Count')
        plt.show()

# Example usage
if __name__ == "__main__":
    dna_sequence = "AGCTAGCCTAGCTAGCTAGC"
    analyzer = DNAAnalyzer(dna_sequence)
    
    print(f"GC Content: {analyzer.gc_content:.2f}%")
    print(f"Reverse Complement: {analyzer.reverse_complement}")
    
    motif = "AGC"
    motif_positions = analyzer.search_motif(motif)
    print(f"Motif '{motif}' found at positions: {motif_positions}")
    
    analyzer.visualize_sequence()
