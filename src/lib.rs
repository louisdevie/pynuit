extern crate minuit;
extern crate pyo3;

use pyo3::prelude::*;

use minuit::app::App;
use minuit::widget::Widget;

#[pyclass]
struct PyWidget {}

#[pyfunction]
fn build_and_run_app(appname: &str, root: &PyWidget) {
    let app = App::new(appname, root.unwrap_widget());
    app.run();
}

#[pymodule]
fn _minuit_py(_py: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_wrapped(wrap_pyfunction!(build_and_run_app))?;
    Ok(())
}
