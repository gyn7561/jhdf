import h5py

import numpy as np

'''
The idea of this test if to write chunked datasets
'''
def write_chunked_datasets(f):
    
    data = np.arange(10500).reshape(7,50,30)

    float_group = f.create_group('float')
    float_group.create_dataset('float32', data=data, dtype='f4', chunks=(2,1,3))
    float_group.create_dataset('float64', data=data, dtype='f8', chunks=(3,4,6))
    
    int_group = f.create_group('int')
    int_group.create_dataset('int8', data=data, dtype='i1', chunks=(5,3,7))
    int_group.create_dataset('int16', data=data, dtype='i2', chunks=(1,1,1))
    int_group.create_dataset('int32', data=data, dtype='i4', chunks=(1,3,9))
    # The idea is to generate a larger B-tree deeper than one level
    int_group.create_dataset('large_int8', data=np.arange(100), dtype='i1', chunks=(1,))

    f.flush()
    f.close()

if __name__ == '__main__':
    print('Making chunked dataset test files...')

    f = h5py.File('test_chunked_datasets_earliest.hdf5', 'w', libver='earliest')
    write_chunked_datasets(f)
    print('created test_chunked_datasets_earliest.hdf5')

# Start working just on 1.8 files first
#     f = h5py.File('test_chunked_datasets_latest.hdf5', 'w', libver='latest')
#     write_chunked_datasets(f)
#     print('created test_chunked_datasets_latest.hdf5')
    