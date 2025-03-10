use arrow2::array::PrimitiveArray;

use crate::{
    array::{BaseArray, DataArray},
    datatypes::DaftNumericType,
};

impl<T> DataArray<T>
where
    T: DaftNumericType,
{
    // applies a native function to a numeric DataArray maintaining validity of the source array.
    pub fn apply<F>(&self, func: F) -> Self
    where
        F: Fn(T::Native) -> T::Native + Copy,
    {
        let arr: &PrimitiveArray<T::Native> = self.data().as_any().downcast_ref().unwrap();
        let result_arr =
            PrimitiveArray::from_trusted_len_values_iter(arr.values_iter().map(|v| func(*v)))
                .with_validity(arr.validity().cloned());

        DataArray::from((self.name(), Box::new(result_arr)))
    }
}
