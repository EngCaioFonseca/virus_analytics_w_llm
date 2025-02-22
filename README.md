# 🧬 Viral Genome Analysis Assistant

## Description
The Viral Genome Analysis Assistant is a powerful web application that combines advanced language models (LLaMA 3.2) with computational biology to analyze viral genomes. This tool helps researchers and biologists understand viral sequences, their structures, mutations, and potential characteristics through an intuitive interface.

## Features

### Core Functionality
- **Genome Sequence Upload**: Support for multiple file formats (FASTA, TXT, GenBank)
- **Interactive Analysis**: Multiple analysis types available simultaneously
- **AI-Powered Insights**: Leverages LLaMA 3.2 for advanced genomic interpretation
- **Real-time Processing**: Immediate feedback and analysis results

### Analysis Types
1. **Basic Genome Information**
   - Sequence composition
   - Length analysis
   - Basic structural features

2. **Protein Structure Analysis**
   - Protein coding regions
   - Structural predictions
   - Functional domains

3. **Mutation Analysis**
   - Variant identification
   - Mutation patterns
   - Potential impact assessment

4. **Phylogenetic Relationships**
   - Evolutionary connections
   - Related viral strains
   - Genetic lineage analysis

5. **Potential Variants**
   - Variant prediction
   - Mutation hotspots
   - Strain classification

6. **Drug Target Sites**
   - Potential therapeutic targets
   - Drug binding sites
   - Treatment implications

### Interactive Features
- **AI Assistant**: Built-in Q&A system for technical support and analysis interpretation
- **Sequence Preview**: Visual representation of uploaded sequences
- **Progress Tracking**: Real-time analysis progress indicators
- **Chat History**: Persistent conversation tracking for reference

## Technical Requirements

### Dependencies

bash

pip install streamlit

pip install requests

pip install biopython

pip install pandas


### Local Setup
1. Install Ollama
2. Download and run the LLaMA 3.2 model:

bash
ollama run llama3.2

3. Run the application:

bash

streamlit run viral_genome_analysis.py


## Usage Guide

### Getting Started
1. Launch the application
2. Upload your viral genome sequence file
3. Select desired analysis types
4. Review results in real-time

### Using the AI Assistant
- Access the sidebar Q&A section for:
  - Technical questions
  - Analysis interpretation
  - Methodology explanations
  - General viral genomics queries

### Supported File Formats
- `.fasta` - FASTA format
- `.txt` - Plain text
- `.gb` - GenBank format

## Best Practices
- Upload clean, verified sequence data
- Select relevant analysis types for your research
- Use the AI assistant for clarification
- Export and save important findings
- Review sequence previews before analysis

## Limitations
- Sequence length limitations may apply
- Analysis depth depends on model capabilities
- Processing time varies with sequence complexity

## Future Enhancements
- Advanced visualization tools
- Batch processing capability
- Database integration
- Comparative analysis features
- Extended file format support
- Enhanced export options

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- New features
- Documentation improvements
- Performance enhancements

## License

MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact
engcaiofonseca@protonmail.com

## Acknowledgments
- LLaMA 3.2 model
- Ollama project
- Streamlit framework
- BioPython library
