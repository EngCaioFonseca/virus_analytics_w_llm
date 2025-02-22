import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from Bio import SeqIO
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np



def query_llama(prompt):
    """
    Send a query to the Ollama API endpoint
    """
    url = "http://localhost:11434/api/generate"  # Corrected Ollama endpoint
    
    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()['response']
    except Exception as e:
        return f"Error: {str(e)}"
    
def plot_sequence_composition(sequence):
    """Generate nucleotide composition plot"""
    counts = Counter(sequence.upper())
    bases = ['A', 'T', 'G', 'C']
    values = [counts[base] for base in bases]
    
    fig = px.pie(
        values=values,
        names=bases,
        title='Nucleotide Composition',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    return fig



def plot_kmer_frequency(sequence, k=3):
    """Plot k-mer frequency distribution"""
    kmers = [sequence[i:i+k] for i in range(len(sequence)-k+1)]
    kmer_counts = Counter(kmers)
    
    # Sort by frequency
    sorted_kmers = dict(sorted(kmer_counts.items(), key=lambda x: x[1], reverse=True)[:20])
    
    fig = px.bar(
        x=list(sorted_kmers.keys()),
        y=list(sorted_kmers.values()),
        title=f'Top {k}-mer Frequencies',
        labels={'x': f'{k}-mer', 'y': 'Frequency'}
    )
    return fig



# Update title and add description
st.title("🧬 Viral Genome Analysis Assistant")
st.markdown("""
    Upload a viral genome sequence to analyze its structure, proteins, mutations, and potential characteristics.
    This tool uses LLaMA 3.2 to provide insights into viral genomics and computational biology analysis.
            Created by Caio Fonseca
""")

# Add visualization options
visualization_options = st.multiselect(
    "Select Visualizations",
    [
        "Sequence Composition",
        "K-mer Frequency Analysis",
        "Codon Usage",
        "Mutation Hotspots",
        "Protein Structure Prediction"
    ]
)

# Add file uploader for genome sequences
uploaded_file = st.file_uploader("Upload Genome Sequence", type=['fasta', 'txt', 'gb'])

if uploaded_file is not None:
    try:
        raw_sequence = uploaded_file.read().decode('utf-8')
        st.success("Genome sequence uploaded successfully!")
        
        # Extract sequence from various formats
        sequence = ""
        try:
            for record in SeqIO.parse(StringIO(raw_sequence), "fasta"):
                sequence = str(record.seq)
        except:
            sequence = raw_sequence.replace('\n', '').replace(' ', '')
        
        # Display sequence preview
        st.subheader("Sequence Preview")
        st.text(sequence[:100] + "...")
        
        # Generate visualizations
        if visualization_options:
            st.subheader("Sequence Visualizations")
            
            for viz in visualization_options:
                if viz == "Sequence Composition":
                    st.plotly_chart(plot_sequence_composition(sequence))
                
                elif viz == "K-mer Frequency Analysis":
                    k = st.slider("K-mer Size", 2, 6, 3)
                    st.plotly_chart(plot_kmer_frequency(sequence, k))
                
                elif viz == "Codon Usage":
                    if len(sequence) % 3 == 0:
                        codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
                        codon_counts = Counter(codons)
                        fig = px.bar(
                            x=list(codon_counts.keys()),
                            y=list(codon_counts.values()),
                            title="Codon Usage Frequency",
                            labels={'x': 'Codon', 'y': 'Frequency'}
                        )
                        st.plotly_chart(fig)
                    else:
                        st.warning("Sequence length is not a multiple of 3 for codon analysis")

        # Continue with existing analysis options...
        
    except Exception as e:
        st.error(f"Error processing genome file: {str(e)}")


# Add analysis options
analysis_type = st.multiselect(
    "Select Analysis Types",
    [
        "Basic Genome Information",
        "Protein Structure Analysis",
        "Mutation Analysis",
        "Phylogenetic Relationships",
        "Potential Variants",
        "Drug Target Sites"
    ]
)

if uploaded_file is not None:
    # Read and process the genome file
    try:
        raw_sequence = uploaded_file.read().decode('utf-8')
        st.success("Genome sequence uploaded successfully!")
        
        # Display sequence preview
        st.subheader("Sequence Preview")
        st.text(raw_sequence[:100] + "...")
        
        # Process selected analyses
        if analysis_type:
            st.subheader("Analysis Results")
            
            for analysis in analysis_type:
                with st.spinner(f"Performing {analysis}..."):
                    # Construct prompt based on analysis type
                    prompt = f"As a computational biology expert, analyze this viral genome sequence for {analysis.lower()}. Sequence: {raw_sequence[:1000]}..."
                    
                    # Get LLaMA response
                    with st.chat_message("assistant"):
                        response = query_llama(prompt)
                        st.markdown(response)
                        
                    # Add to chat history
                    if "messages" not in st.session_state:
                        st.session_state.messages = []
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    st.session_state.messages.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"Error processing genome file: {str(e)}")

# Add sidebar with additional information
with st.sidebar:
    st.header("About")
    st.markdown("""
        This tool helps researchers analyze viral genomes using advanced AI techniques.
        
        **Capabilities:**
        - Basic genome analysis
        - Protein structure prediction
        - Mutation identification
        - Phylogenetic analysis
        - Variant detection
        - Drug target identification
        
        **Supported File Formats:**
        - FASTA (.fasta)
        - Plain text (.txt)
        - GenBank (.gb)
    """)

        # Add Q&A section in sidebar
    st.markdown("---")  # Divider
    st.header("Ask a Question")
    st.markdown("""
        Need help? Ask anything about:
        - The analysis results
        - Viral genomics
        - How to use this tool
        - Computational biology
    """)
    
    # Initialize sidebar chat history if not exists
    if "sidebar_messages" not in st.session_state:
        st.session_state.sidebar_messages = []
    
    # Display sidebar chat history
    for message in st.session_state.sidebar_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Add question input to sidebar
    sidebar_prompt = st.text_area("Your question:", height=100)
    if st.button("Ask"):
        if sidebar_prompt:
            # Display user question
            with st.chat_message("user"):
                st.markdown(sidebar_prompt)
            
            # Get LLaMA response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Construct context-aware prompt
                    context = ""
                    if "current_sequence" in st.session_state:
                        context = f"\nContext: Working with viral genome sequence. "
                    
                    full_prompt = f"You are a computational biology and viral genomics expert. {context}Question: {sidebar_prompt}"
                    response = query_llama(full_prompt)
                    st.markdown(response)
            
            # Add to sidebar chat history
            st.session_state.sidebar_messages.append({"role": "user", "content": sidebar_prompt})
            st.session_state.sidebar_messages.append({"role": "assistant", "content": response})
