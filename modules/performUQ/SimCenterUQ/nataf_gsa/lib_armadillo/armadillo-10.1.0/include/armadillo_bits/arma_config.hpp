// Copyright 2008-2016 Conrad Sanderson (http://conradsanderson.id.au)
// Copyright 2008-2016 National ICT Australia (NICTA)
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ------------------------------------------------------------------------


//! \addtogroup arma_config
//! @{

#define ARMA_USE_LAPACK
#define ARMA_USE_BLAS

struct arma_config
  {
  #if defined(ARMA_MAT_PREALLOC)
    static constexpr uword mat_prealloc = (sword(ARMA_MAT_PREALLOC) > 0) ? uword(ARMA_MAT_PREALLOC) : 1;
  #else
    static constexpr uword mat_prealloc = 16;
  #endif
  
  
  #if defined(ARMA_OPENMP_THRESHOLD)
    static constexpr uword mp_threshold = (sword(ARMA_OPENMP_THRESHOLD) > 0) ? uword(ARMA_OPENMP_THRESHOLD) : 240;
  #else
    static constexpr uword mp_threshold = 240;
  #endif
  
  
  #if defined(ARMA_OPENMP_THREADS)
    static constexpr uword mp_threads = (sword(ARMA_OPENMP_THREADS) > 0) ? uword(ARMA_OPENMP_THREADS) : 10;
  #else
    static constexpr uword mp_threads = 10;
  #endif
  
  
  #if defined(ARMA_USE_ATLAS)
    static constexpr bool atlas = true;
  #else
    static constexpr bool atlas = false;
  #endif
  
  
  #if defined(ARMA_USE_LAPACK)
    static constexpr bool lapack = true;
  #else
    static constexpr bool lapack = false;
  #endif
  
  
  #if defined(ARMA_USE_BLAS)
    static constexpr bool blas = true;
  #else
    static constexpr bool blas = false;
  #endif
  
  
  #if defined(ARMA_USE_NEWARP)
    static constexpr bool newarp = true;
  #else
    static constexpr bool newarp = false;
  #endif
  
  
  #if defined(ARMA_USE_ARPACK)
    static constexpr bool arpack = true;
  #else
    static constexpr bool arpack = false;
  #endif
  
  
  #if defined(ARMA_USE_SUPERLU)
    static constexpr bool superlu = true;
  #else
    static constexpr bool superlu = false;
  #endif
  
  
  #if defined(ARMA_USE_HDF5)
    static constexpr bool hdf5 = true;
  #else
    static constexpr bool hdf5 = false;
  #endif
  
  
  #if defined(ARMA_NO_DEBUG)
    static constexpr bool debug = false;
  #else
    static constexpr bool debug = true;
  #endif
  
  
  #if defined(ARMA_EXTRA_DEBUG)
    static constexpr bool extra_debug = true;
  #else
    static constexpr bool extra_debug = false;
  #endif
  
  
  #if defined(ARMA_GOOD_COMPILER)
    static constexpr bool good_comp = true;
  #else
    static constexpr bool good_comp = false;
  #endif
  
  
  #if (  \
         defined(ARMA_EXTRA_MAT_PROTO)   || defined(ARMA_EXTRA_MAT_MEAT)   \
      || defined(ARMA_EXTRA_COL_PROTO)   || defined(ARMA_EXTRA_COL_MEAT)   \
      || defined(ARMA_EXTRA_ROW_PROTO)   || defined(ARMA_EXTRA_ROW_MEAT)   \
      || defined(ARMA_EXTRA_CUBE_PROTO)  || defined(ARMA_EXTRA_CUBE_MEAT)  \
      || defined(ARMA_EXTRA_FIELD_PROTO) || defined(ARMA_EXTRA_FIELD_MEAT) \
      || defined(ARMA_EXTRA_SPMAT_PROTO) || defined(ARMA_EXTRA_SPMAT_MEAT) \
      || defined(ARMA_EXTRA_SPCOL_PROTO) || defined(ARMA_EXTRA_SPCOL_MEAT) \
      || defined(ARMA_EXTRA_SPROW_PROTO) || defined(ARMA_EXTRA_SPROW_MEAT) \
      )
    static constexpr bool extra_code = true;
  #else
    static constexpr bool extra_code = false;
  #endif
  
  
  #if defined(ARMA_HAVE_CXX14)
    static constexpr bool cxx14 = true;
  #else
    static constexpr bool cxx14 = false;
  #endif
  
  
  #if defined(ARMA_HAVE_CXX17)
    static constexpr bool cxx17 = true;
  #else
    static constexpr bool cxx17 = false;
  #endif
  
  
  #if (!defined(ARMA_DONT_USE_STD_MUTEX))
    static constexpr bool std_mutex = true;
  #else
    static constexpr bool std_mutex = false;
  #endif
  
  
  #if (defined(_POSIX_C_SOURCE) && (_POSIX_C_SOURCE >= 200112L))
    static constexpr bool posix = true;
  #else
    static constexpr bool posix = false;
  #endif
  
  
  #if defined(ARMA_USE_WRAPPER)
    static constexpr bool wrapper = true;
  #else
    static constexpr bool wrapper = false;
  #endif
  
  
  #if defined(ARMA_USE_OPENMP)
    static constexpr bool openmp = true;
  #else
    static constexpr bool openmp = false;
  #endif
  
  
  #if defined(ARMA_USE_FORTRAN_HIDDEN_ARGS)
    static constexpr bool hidden_args = true;
  #else
    static constexpr bool hidden_args = false;
  #endif
  };



//! @}