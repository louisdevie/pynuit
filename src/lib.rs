use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn add(a: u32, b: u32) -> u32 {
    a + b
}

#[pymodule]
fn minuit_py(_py: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_wrapped(wrap_pyfunction!(add))?;
    Ok(())
}
