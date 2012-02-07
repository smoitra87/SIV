""" 
Various methods and objects to deal with the SIV sequence

@author: smoitra@cs.cmu.edu 
BSD License

Definite Features
* Load the Fasta sequence 
* Gap strip a sequence 
* Identify all characters in the alignment
* Calculate the consensus sequence of the alignment
* Blast a sequence
* Translate a nt seq usign best ORF

* Refine the alignment ? 
* Gap strip the entire alignment ? 


"""

from Bio import AlignIO
from Bio.Align import AlignInfo


import os,sys
import logging
import utility as util




class SIVHandler(object) : 
	""" Defines members and methods for SIV alignment class"""
	def __init__(self,alnf) : 
		""" Inits the siv class
			alnf: alignment input file (fasta preferred)
		"""
		self.logger = logging.getLogger("siv.hlr")
		self.logger.info("Initing the SIVHandler class")
		try : 
			self.aln = AlignIO.read(alnf,"fasta")
		except IOError:
			sys.stderr.writeline("Can't read alignment file%s" %
			(alnf))
			pass
			
		self.aln_fname = alnf
		# Store all info about the alignment
		self.alninfo = AlignInfo.SummaryInfo(self.aln)
	
	def get_all_letters(self) : 
		""" Returns all the letters contained in the alignment"""
		return self.alninfo._get_all_letters()

	def set_consensus(self,dumb=True) : 
		""" Returns the consensus sequence
		Ambiguous letters are printed as N
		This is an expensive operation. So is only called on demand
		"""
		self.logger.info('Calculating Consensus. Gonna Take time..!')
		if dumb : 
			self.consensus = self.alninfo.dumb_consensus(ambiguous='N') 
		else :
			self.consensus = self.alninfo.gap_consensus(ambiguous='N')
		self.logger.info('Done calculating consensus')

if __name__ == '__main__'	 :
	aln_fname = os.path.join(util.datadir,'siv1.fasta')
	sivh = SIVHandler(aln_fname)
	# Calculate the consensus
	#sivh.set_consensus()

