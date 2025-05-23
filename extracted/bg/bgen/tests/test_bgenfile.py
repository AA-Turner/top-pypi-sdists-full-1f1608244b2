
from pathlib import Path
import unittest

import numpy as np

from bgen import BgenReader

from tests.utils import load_gen_data

class TestBgenReader(unittest.TestCase):
    ''' class to make sure BgenReader works correctly
    '''
    
    @classmethod
    def setUpClass(cls):
        cls.gen_data = load_gen_data()
    
    def setUp(self):
        ''' set path to folder with test data
        '''
        self.folder = Path(__file__).parent /  "data"
    
    def test_context_handler_closed_bgen_samples(self):
        ''' no samples available from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile.samples) > 0)
        
        with self.assertRaises(ValueError):
            bfile.samples
    
    def test_context_handler_closed_bgen_varids(self):
        ''' no varids available from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile.varids()) > 0)
        
        with self.assertRaises(ValueError):
            bfile.varids()
    
    def test_context_handler_closed_bgen_rsids(self):
        ''' no rsids available from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile.rsids()) > 0)
        
        with self.assertRaises(ValueError):
            bfile.rsids()
    
    def test_context_handler_closed_bgen_positions(self):
        ''' no positions available from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile.positions()) > 0)
        
        with self.assertRaises(ValueError):
            bfile.positions()
    
    def test_context_handler_closed_bgen_length(self):
        ''' error raised if accessing length of exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile) > 0)
        
        with self.assertRaises(ValueError):
             len(bfile)
    
    def test_context_handler_closed_bgen_slice(self):
        ''' error raised if slicing variant from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile) > 0)
        
        with self.assertRaises(ValueError):
             var = bfile[0]
    
    def test_context_handler_closed_bgen_at_position(self):
        ''' error raised if getting variant at position from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile) > 0)
        
        with self.assertRaises(ValueError):
             var = bfile.at_position(100)
    
    def test_context_handler_closed_bgen_with_rsid(self):
        ''' error raised if getting variant with rsid from exited BgenReader
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            self.assertTrue(len(bfile) > 0)
        
        with self.assertRaises(ValueError):
             var = bfile.with_rsid('rs111')
    
    def test_context_handler_variant_data_not_loaded(self):
        ''' error raised if we try to access variant data after closing BgenFile
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            var = next(bfile)
        
        with self.assertRaises(ValueError):
            # cannot access data after file closed
            var.minor_allele_dosage
    
    def test_context_handler_variant_data_loaded(self):
        '''no error raised for variant from closed BgenReader, IF data is already loaded
        '''
        path = self.folder / 'example.16bits.zstd.bgen'
        with BgenReader(path) as bfile:
            var = next(bfile)
            var.minor_allele_dosage # load data while file still open
        
        # can access data after file closed, but only because the file was read 
        # previously while still open
        dose = var.minor_allele_dosage
        self.assertTrue(isinstance(dose, np.ndarray))
    
    def test_fetch(self):
        ''' can fetch variants within a genomic region
        '''
        chrom, start, stop = '01', 5000, 50000
        bfile = BgenReader(self.folder / 'example.16bits.bgen')
        self.assertTrue(bfile._check_for_index(str(self.folder / 'example.16bits.bgen')))
        
        self.assertTrue(list(bfile.fetch('02')) == [])
    
    def test_fetch_whole_chrom(self):
        ''' fetching just with chrom gives all variants on chromosome
        '''
        chrom, start, stop = '01', 5000, 50000
        bfile = BgenReader(self.folder / 'example.16bits.bgen')
        
        # test fetching a whole chromosome
        sortkey = lambda x: (x.chrom, x.pos)
        for x, y in zip(sorted(bfile.fetch(chrom), key=sortkey), sorted(self.gen_data, key=sortkey)):
            self.assertEqual(x.rsid, y.rsid)
            self.assertEqual(x.chrom, y.chrom)
            self.assertEqual(x.pos, y.pos)
    
    def test_fetch_after_position(self):
        ''' fetching variants with chrom and start gives all variants after pos
        '''
        chrom, start, stop = '01', 5000, 50000
        bfile = BgenReader(self.folder / 'example.16bits.bgen')
        
        sortkey = lambda x: (x.chrom, x.pos)
        gen_vars = [x for x in sorted(self.gen_data, key=sortkey) if start <= x.pos]
        for x, y in zip(sorted(bfile.fetch(chrom, start), key=sortkey), gen_vars):
            self.assertEqual(x.rsid, y.rsid)
            self.assertEqual(x.chrom, y.chrom)
            self.assertEqual(x.pos, y.pos)
    
    def test_fetch_in_region(self):
        ''' fetching variants with chrom, start, stop gives variants in region
        '''
        chrom, start, stop = '01', 5000, 50000
        bfile = BgenReader(self.folder / 'example.16bits.bgen')
        
        sortkey = lambda x: (x.chrom, x.pos)
        gen_vars = [x for x in sorted(self.gen_data, key=sortkey) if start <= x.pos <= stop]
        for x, y in zip(sorted(bfile.fetch(chrom, start, stop), key=sortkey), gen_vars):
            self.assertEqual(x.rsid, y.rsid)
            self.assertEqual(x.chrom, y.chrom)
            self.assertEqual(x.pos, y.pos)
        
        # check that we don't get any variants in a region without any
        self.assertEqual(list(bfile.fetch(chrom, start * 1000, stop * 1000)), [])
