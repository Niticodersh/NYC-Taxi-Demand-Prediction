# Taxi Demand Prediction with Improved Seasonal Patterns Learning

## Problem Statement
Taxi demand prediction is a classic time series forecasting problem. Our aim is to enhance existing sequence models to better capture the inherent periodicity in time series data. We propose novel techniques and conduct experiments to demonstrate performance improvements.

## Solution Statement
Our solution is divided into several stages, each introducing new methods to enhance model performance:
1. **Stage 1**: Initial attempts with AutoRegressive Integrated Moving Average (ARIMA) models reveal limitations due to linear nature and fail to perform well. Refer to `ARIMA.ipynb` jupyter notebook.
2. **Stage 2**: Introduction of deep learning models (LSTM, RNN, GRU) trained on a comprehensive dataset with various features related to taxi trips. Refer to `vanilla_deep_learning_models.ipynb` jupyter notebook.
3. **Stage 3**: Improved integration of seasonality by splitting model networks into separate streams for continuous and seasonal data, resulting in better capture of seasonal patterns. Refer to `SeasonalityModels.ipynb` jupyter notebook.
4. **Stage 4**: Introduction of Periodicity-preserving Sequences (PPS), a novel representation that captures periodicity by spanning sequences across multiple years. Refer to `SeasonalityModels.ipynb` jupyter notebook.

## Dataset
We utilize a dataset comprising trip records from yellow taxis operating in New York City. The dataset includes various features such as pick-up/drop-off dates, locations, distances traveled, fares, and passenger counts. Preprocessing steps include handling missing values, removing erroneous data, and normalization. Final pre-processed dataset used : `normalised_data.parquet`

## Major Innovations/Contributions
- **Seasonal Net**: Architecture incorporating separate networks for continuous and seasonal data, enhancing seasonality capture.
- **Periodicity-preserving Sequences (PPS)**: Representation of input sequences across multiple years, aiding in better understanding of periodicity.

## Results
Evaluation using Mean Squared Error (MSE) metric demonstrates performance improvements:
### Vanilla Models
| Model | LSTM   | RNN    | GRU    |
|-------|--------|--------|--------|
| MSE   | 0.000601 | 0.00227 | 0.00221 |

### Models with SeasonalNet
| Model | LSTM   | RNN    | GRU    |
|-------|--------|--------|--------|
| MSE   | 0.000277 | 0.000276 | 0.000323 |

### Normal Sequences
| Model | LSTM with Seasonal Net | RNN with Seasonal Net | GRU with Seasonal Net |
|-------|--------------------------|------------------------|-----------------------|
| MSE   | 0.000277                 | 0.000276               | 0.000323              |

### Periodicity-preserving Sequences (PPS)
| Model | LSTM with Seasonal Net | RNN with Seasonal Net | GRU with Seasonal Net |
|-------|--------------------------|------------------------|-----------------------|
| MSE   | 0.000273                 | 0.000269               | 0.000281              |


## Conclusion
Our work demonstrates the effectiveness of separate models for ordinal and continuous numerical data, along with innovative sequence representation techniques. These approaches are architecture-independent and applicable to various time series forecasting tasks, providing insights into periodicity in data.
