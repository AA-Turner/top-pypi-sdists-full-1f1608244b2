import logging
import math
from collections import OrderedDict
from functools import reduce
from typing import Dict, List, Optional, Union

import numpy as np
import pytorch_lightning as pl
import torch
import torch.nn as nn
import torchmetrics

from neuralprophet import configure, np_types
from neuralprophet.components.router import get_future_regressors, get_seasonality, get_trend
from neuralprophet.utils import (
    check_for_regularization,
    config_events_to_model_dims,
    reg_func_events,
    reg_func_regressors,
    reg_func_season,
    reg_func_seasonality_glocal,
    reg_func_trend,
    reg_func_trend_glocal,
)
from neuralprophet.utils_torch import init_parameter, interprete_model

log = logging.getLogger("NP.time_net")


class TimeNet(pl.LightningModule):
    """Linear time regression fun and some not so linear fun.
    A modular model that models classic time-series components
        * trend
        * seasonality
        * auto-regression (as AR-Net)
        * covariates (as AR-Net)
        * apriori regressors
        * events and holidays
    by using Neural Network components.
    The Auto-regression and covariate components can be configured as a deeper network (AR-Net).
    """

    def __init__(
        self,
        config_seasonality: configure.ConfigSeasonality,
        config_train: Optional[configure.Train] = None,
        config_trend: Optional[configure.Trend] = None,
        config_ar: Optional[configure.AR] = None,
        config_normalization: Optional[configure.Normalization] = None,
        config_lagged_regressors: Optional[configure.ConfigLaggedRegressors] = None,
        config_regressors: Optional[configure.ConfigFutureRegressors] = None,
        config_events: Optional[configure.ConfigEvents] = None,
        config_holidays: Optional[configure.ConfigCountryHolidays] = None,
        n_forecasts: int = 1,
        n_lags: int = 0,
        max_lags: int = 0,
        ar_layers: Optional[List[int]] = [],
        lagged_reg_layers: Optional[List[int]] = [],
        compute_components_flag: bool = False,
        metrics: Optional[np_types.CollectMetricsMode] = {},
        id_list: List[str] = ["__df__"],
        num_trends_modelled: int = 1,
        num_seasonalities_modelled: int = 1,
        num_seasonalities_modelled_dict: dict = None,
        meta_used_in_model: bool = False,
    ):
        """
        Parameters
        ----------
            quantiles : list
                the set of quantiles estimated
            config_train : configure.Train
            config_trend : configure.Trend
            config_seasonality : configure.ConfigSeasonality
            config_ar : configure.AR
            config_lagged_regressors : configure.ConfigLaggedRegressors
                Configurations for lagged regressors
            config_regressors : configure.ConfigFutureRegressors
                Configs of regressors with mode and index.
            config_events : configure.ConfigEvents
            config_holidays : OrderedDict
            config_normalization: OrderedDict
            n_forecasts : int
                number of steps to forecast. Aka number of model outputs
            n_lags : int
                number of previous steps of time series used as input (aka AR-order)
                Note
                ----
                The default value is ``0``, which initializes no auto-regression.

            max_lags : int
                Number of max. previous steps of time series used as input (aka AR-order).

            ar_layers : list
                List of hidden layers (for AR-Net).

                Note
                ----
                The default value is ``[]``, which initializes no hidden layers.

            lagged_reg_layers : list
                List of hidden layers (for covariate-Net).

                Note
                ----
                The default value is ``[]``, which initializes no hidden layers.


            compute_components_flag : bool
                Flag whether to compute the components of the model or not.
            metrics : dict
                Dictionary of torchmetrics to be used during training and for evaluation.
            id_list : list
                List of different time series IDs, used for global-local modelling (if enabled)
                Note
                ----
                This parameter is set to  ``['__df__']`` if only one time series is input.
            num_trends_modelled : int
                Number of different trends modelled.
                Note
                ----
                If only 1 time series is modelled, it will be always 1.
                Note
                ----
                For multiple time series. If trend is modelled globally the value is set
                to 1, otherwise it is set to the number of time series modelled.
            num_seasonalities_modelled : int
                Number of different seasonalities modelled.
                Note
                ----
                If only 1 time series is modelled, it will be always 1.
                Note
                ----
                For multiple time series. If seasonality is modelled globally the value is set
                to 1, otherwise it is set to the number of time series modelled.
            meta_used_in_model : boolean
                Whether we need to know the time series ID when we interact with the Model.
                Note
                ----
                Will be set to ``True`` if more than one component is modelled locally.
        """
        super().__init__()

        # Store hyerparameters in model checkpoint
        # TODO: causes a RuntimeError under certain conditions, investigate and handle better
        try:
            self.save_hyperparameters()
        except RuntimeError:
            pass

        # General
        self.n_forecasts = n_forecasts

        # Lightning Config
        self.config_train = config_train
        self.config_normalization = config_normalization
        self.compute_components_flag = compute_components_flag

        # Optimizer and LR Scheduler
        self._optimizer = self.config_train.optimizer
        self._scheduler = self.config_train.scheduler
        self.automatic_optimization = False

        # Hyperparameters (can be tuned using trainer.tune())
        self.learning_rate = self.config_train.learning_rate if self.config_train.learning_rate is not None else 1e-3
        self.batch_size = self.config_train.batch_size

        # Metrics Config
        self.metrics_enabled = bool(metrics)  # yields True if metrics is not an empty dictionary
        if self.metrics_enabled:
            metrics = {metric: torchmetrics.__dict__[metrics[metric][0]](**metrics[metric][1]) for metric in metrics}
            self.log_args = {
                "on_step": False,
                "on_epoch": True,
                "prog_bar": True,
                "batch_size": self.config_train.batch_size,
            }
            self.metrics_train = torchmetrics.MetricCollection(metrics=metrics)
            self.metrics_val = torchmetrics.MetricCollection(metrics=metrics, postfix="_val")

        # For Multiple Time Series Analysis
        self.id_list = id_list
        self.id_dict = dict((key, i) for i, key in enumerate(id_list))
        self.num_trends_modelled = num_trends_modelled
        self.num_seasonalities_modelled = num_seasonalities_modelled
        self.num_seasonalities_modelled_dict = num_seasonalities_modelled_dict
        self.meta_used_in_model = meta_used_in_model

        # Regularization
        self.reg_enabled = check_for_regularization(
            [
                config_seasonality,
                config_regressors,
                config_lagged_regressors,
                config_ar,
                config_events,
                config_trend,
                config_holidays,
            ]
        )

        # Quantiles
        self.quantiles = self.config_train.quantiles

        # Trend
        self.config_trend = config_trend
        self.trend = get_trend(
            config=config_trend,
            id_list=id_list,
            quantiles=self.quantiles,
            num_trends_modelled=num_trends_modelled,
            n_forecasts=n_forecasts,
            device=self.device,
        )

        # Seasonalities
        self.config_seasonality = config_seasonality
        # Error handling
        if self.config_seasonality is not None:
            if self.config_seasonality.mode == "multiplicative" and self.config_trend is None:
                raise ValueError("Multiplicative seasonality requires trend.")
            if self.config_seasonality.mode not in ["additive", "multiplicative"]:
                raise ValueError(f"Seasonality Mode {self.config_seasonality.mode} not implemented.")
            # Initialize seasonality
            self.seasonality = get_seasonality(
                config=config_seasonality,
                id_list=id_list,
                quantiles=self.quantiles,
                num_seasonalities_modelled=num_seasonalities_modelled,
                num_seasonalities_modelled_dict=num_seasonalities_modelled_dict,
                n_forecasts=n_forecasts,
                device=self.device,
            )

        # Events
        self.config_events = config_events
        self.config_holidays = config_holidays
        self.events_dims = config_events_to_model_dims(self.config_events, self.config_holidays)
        if self.events_dims is not None:
            n_additive_event_params = 0
            n_multiplicative_event_params = 0
            for event, configs in self.events_dims.items():
                if configs["mode"] not in ["additive", "multiplicative"]:
                    log.error("Event Mode {} not implemented. Defaulting to 'additive'.".format(configs["mode"]))
                    self.events_dims[event]["mode"] = "additive"
                if configs["mode"] == "additive":
                    n_additive_event_params += len(configs["event_indices"])
                elif configs["mode"] == "multiplicative":
                    if self.config_trend is None:
                        log.error("Multiplicative events require trend.")
                        raise ValueError
                    n_multiplicative_event_params += len(configs["event_indices"])
            self.event_params = nn.ParameterDict(
                {
                    # dimensions - [no. of quantiles, no. of additive events]
                    "additive": init_parameter(dims=[len(self.quantiles), n_additive_event_params]),
                    # dimensions - [no. of quantiles, no. of multiplicative events]
                    "multiplicative": init_parameter(dims=[len(self.quantiles), n_multiplicative_event_params]),
                }
            )
        else:
            self.config_events = None
            self.config_holidays = None

        # Autoregression
        self.config_ar = config_ar
        self.n_lags = n_lags
        self.ar_layers = ar_layers
        self.max_lags = max_lags
        if self.n_lags > 0:
            self.ar_net = nn.ModuleList()
            d_inputs = self.n_lags
            for d_hidden_i in self.ar_layers:
                self.ar_net.append(nn.Linear(d_inputs, d_hidden_i, bias=True))
                d_inputs = d_hidden_i
            # final layer has input size d_inputs and output size equal to no. of forecasts * no. of quantiles
            self.ar_net.append(nn.Linear(d_inputs, self.n_forecasts * len(self.quantiles), bias=False))
            for lay in self.ar_net:
                nn.init.kaiming_normal_(lay.weight, mode="fan_in")

        # Lagged regressors
        self.lagged_reg_layers = lagged_reg_layers
        self.config_lagged_regressors = config_lagged_regressors
        if self.config_lagged_regressors is not None:
            self.covar_net = nn.ModuleList()
            d_inputs = sum([covar.n_lags for _, covar in self.config_lagged_regressors.items()])
            for d_hidden_i in self.lagged_reg_layers:
                self.covar_net.append(nn.Linear(d_inputs, d_hidden_i, bias=True))
                d_inputs = d_hidden_i
            self.covar_net.append(nn.Linear(d_inputs, self.n_forecasts * len(self.quantiles), bias=False))
            for lay in self.covar_net:
                nn.init.kaiming_normal_(lay.weight, mode="fan_in")

        # Regressors
        self.config_regressors = config_regressors
        if self.config_regressors.regressors is not None:
            # Initialize future_regressors
            self.future_regressors = get_future_regressors(
                config=config_regressors,
                id_list=id_list,
                quantiles=self.quantiles,
                n_forecasts=n_forecasts,
                device=self.device,
                config_trend_none_bool=self.config_trend is None,
            )
        else:
            self.config_regressors.regressors = None

    @property
    def ar_weights(self) -> torch.Tensor:
        """sets property auto-regression weights for regularization. Update if AR is modelled differently"""
        # TODO: this is wrong for deep networks, use utils_torch.interprete_model
        return self.ar_net[0].weight

    def get_covar_weights(self, covar_input=None) -> torch.Tensor:
        """
        Get attributions of covariates network w.r.t. the model input.
        """
        if self.config_lagged_regressors is not None:
            # Accumulate the lags of the covariates
            covar_splits = np.add.accumulate(
                [covar.n_lags for _, covar in self.config_lagged_regressors.items()][:-1]
            ).tolist()
            # If actual covariates are provided, use them to compute the attributions
            if covar_input is not None:
                covar_input = torch.cat([covar for _, covar in covar_input.items()], axis=1)
            # Calculate the attributions w.r.t. the inputs
            if self.lagged_reg_layers == []:
                attributions = self.covar_net[0].weight
            else:
                attributions = interprete_model(self, "covar_net", "forward_covar_net", covar_input)
            # Split the attributions into the different covariates
            attributions_split = torch.tensor_split(
                attributions,
                covar_splits,
                axis=1,
            )
            # Combine attributions and covariate name
            covar_attributions = dict(zip(self.config_lagged_regressors.keys(), attributions_split))
        else:
            covar_attributions = None
        return covar_attributions

    def set_covar_weights(self, covar_weights: torch.Tensor):
        """
        Function to set the covariate weights for later interpretation in compute_components.
        This function is needed since the gradient information is not available during the predict_step
        method and attributions cannot be calculated in compute_components.

        :param covar_weights: _description_
        :type covar_weights: torch.Tensor
        """
        self.covar_weights = covar_weights

    def get_event_weights(self, name: str) -> Dict[str, torch.Tensor]:
        """
        Retrieve the weights of event features given the name
        Parameters
        ----------
            name : str
                Event name
        Returns
        -------
            OrderedDict
                Dict of the weights of all offsets corresponding to a particular event
        """

        event_dims = self.events_dims[name]
        mode = event_dims["mode"]

        if mode == "multiplicative":
            event_params = self.event_params["multiplicative"]
        else:
            assert mode == "additive"
            event_params = self.event_params["additive"]

        event_param_dict = OrderedDict({})
        for event_delim, indices in zip(event_dims["event_delim"], event_dims["event_indices"]):
            event_param_dict[event_delim] = event_params[:, indices : (indices + 1)]
        return event_param_dict

    def _compute_quantile_forecasts_from_diffs(self, diffs: torch.Tensor, predict_mode: bool = False) -> torch.Tensor:
        """
        Computes the actual quantile forecasts from quantile differences estimated from the model
        Args:
            diffs : torch.Tensor
                tensor of dims (batch, n_forecasts, no_quantiles) which
                contains the median quantile forecasts as well as the diffs of other quantiles
                from the median quantile
            predict_mode : bool
                boolean variable indicating whether the model is in prediction mode
        Returns:
            dim (batch, n_forecasts, no_quantiles)
                final forecasts
        """
        if len(self.quantiles) > 1:
            # generate the actual quantile forecasts from predicted differences
            if any(quantile > 0.5 for quantile in self.quantiles):
                quantiles_divider_index = next(i for i, quantile in enumerate(self.quantiles) if quantile > 0.5)
            else:
                quantiles_divider_index = len(self.quantiles)

            n_upper_quantiles = diffs.shape[-1] - quantiles_divider_index
            n_lower_quantiles = quantiles_divider_index - 1

            out = torch.zeros_like(diffs)
            out[:, :, 0] = diffs[:, :, 0]  # set the median where 0 is the median quantile index

            if n_upper_quantiles > 0:  # check if upper quantiles exist
                upper_quantile_diffs = diffs[:, :, quantiles_divider_index:]
                if predict_mode:  # check for quantile crossing and correct them in predict mode
                    upper_quantile_diffs[:, :, 0] = torch.max(
                        torch.tensor(0, device=self.device), upper_quantile_diffs[:, :, 0]
                    )
                    for i in range(n_upper_quantiles - 1):
                        next_diff = upper_quantile_diffs[:, :, i + 1]
                        diff = upper_quantile_diffs[:, :, i]
                        upper_quantile_diffs[:, :, i + 1] = torch.max(next_diff, diff)
                out[:, :, quantiles_divider_index:] = (
                    upper_quantile_diffs + diffs[:, :, 0].unsqueeze(dim=2).repeat(1, 1, n_upper_quantiles).detach()
                )  # set the upper quantiles

            if n_lower_quantiles > 0:  # check if lower quantiles exist
                lower_quantile_diffs = diffs[:, :, 1:quantiles_divider_index]
                if predict_mode:  # check for quantile crossing and correct them in predict mode
                    lower_quantile_diffs[:, :, -1] = torch.max(
                        torch.tensor(0, device=self.device), lower_quantile_diffs[:, :, -1]
                    )
                    for i in range(n_lower_quantiles - 1, 0, -1):
                        next_diff = lower_quantile_diffs[:, :, i - 1]
                        diff = lower_quantile_diffs[:, :, i]
                        lower_quantile_diffs[:, :, i - 1] = torch.max(next_diff, diff)
                lower_quantile_diffs = -lower_quantile_diffs
                out[:, :, 1:quantiles_divider_index] = (
                    lower_quantile_diffs + diffs[:, :, 0].unsqueeze(dim=2).repeat(1, 1, n_lower_quantiles).detach()
                )  # set the lower quantiles
        else:
            out = diffs
        return out

    def scalar_features_effects(self, features: torch.Tensor, params: nn.Parameter, indices=None) -> torch.Tensor:
        """
        Computes events component of the model
        Parameters
        ----------
            features : torch.Tensor, float
                Features (either additive or multiplicative) related to event component dims (batch, n_forecasts,
                n_features)
            params : nn.Parameter
                Params (either additive or multiplicative) related to events
            indices : list of int
                Indices in the feature tensors related to a particular event
        Returns
        -------
            torch.Tensor
                Forecast component of dims (batch, n_forecasts)
        """
        if indices is not None:
            features = features[:, :, indices]
            params = params[:, indices]

        return torch.sum(features.unsqueeze(dim=2) * params.unsqueeze(dim=0).unsqueeze(dim=0), dim=-1)

    def auto_regression(self, lags: Union[torch.Tensor, float]) -> torch.Tensor:
        """Computes auto-regessive model component AR-Net.
        Parameters
        ----------
            lags  : torch.Tensor, float
                Previous times series values, dims: (batch, n_lags)
        Returns
        -------
            torch.Tensor
                Forecast component of dims: (batch, n_forecasts)
        """
        x = lags
        for i in range(len(self.ar_layers) + 1):
            if i > 0:
                x = nn.functional.relu(x)
            x = self.ar_net[i](x)

        # segment the last dimension to match the quantiles
        x = x.reshape(x.shape[0], self.n_forecasts, len(self.quantiles))
        return x

    def forward_covar_net(self, covariates):
        """Compute all covariate components.
        Parameters
        ----------
            covariates : dict(torch.Tensor, float)
                dict of named covariates (keys) with their features (values)
                dims of each dict value: (batch, n_lags)
        Returns
        -------
            torch.Tensor
                Forecast component of dims (batch, n_forecasts, quantiles)
        """
        # Concat covariates into one tensor)
        if isinstance(covariates, dict):
            x = torch.cat([covar for _, covar in covariates.items()], axis=1)
        else:
            x = covariates
        for i in range(len(self.lagged_reg_layers) + 1):
            if i > 0:
                x = nn.functional.relu(x)
            x = self.covar_net[i](x)

        # segment the last dimension to match the quantiles
        x = x.reshape(x.shape[0], self.n_forecasts, len(self.quantiles))
        return x

    def forward(self, inputs: Dict, meta: Dict = None, compute_components_flag: bool = False) -> torch.Tensor:
        """This method defines the model forward pass.
        Note
        ----
        Time input is required. Minimum model setup is a linear trend.
        Parameters
        ----------
            inputs : dict
                Model inputs, each of len(df) but with varying dimensions
                Note
                ----
                Contains the following data:
                Model Inputs
                    * ``time`` (torch.Tensor , loat), normalized time, dims: (batch, n_forecasts)
                    * ``lags`` (torch.Tensor, float), dims: (batch, n_lags)
                    * ``seasonalities`` (torch.Tensor, float), dict of named seasonalities (keys) with their features
                    (values), dims of each dict value (batch, n_forecasts, n_features)
                    * ``covariates`` (torch.Tensor, float), dict of named covariates (keys) with their features
                    (values), dims of each dict value: (batch, n_lags)
                    * ``events`` (torch.Tensor, float), all event features, dims (batch, n_forecasts, n_features)
                    * ``regressors``(torch.Tensor, float), all regressor features, dims (batch, n_forecasts, n_features)
                    * ``predict_mode`` (bool), optional and only passed during prediction
            meta : dict, default=None
                Metadata about the all the samples of the model input batch.
                Contains the following:
                Model Meta:
                    * ``df_name`` (list, str), time series ID corresponding to each sample of the input batch.
                Note
                ----
                The meta is sorted in the same way the inputs are sorted.
                Note
                ----
                The default None value allows the forward method to be used without providing the meta argument.
                This was designed to avoid issues with the library `lr_finder` https://github.com/davidtvs/pytorch-lr-finder
                while having  ``config_trend.trend_global_local="local"``.
                The turnaround consists on passing the same meta (dummy ID) to all the samples of the batch.
                Internally, this is equivalent to use ``config_trend.trend_global_local="global"`` to find the optimal
                learning rate.
            compute_components_flag : bool, default=False
                If True, components will be computed.

        Returns
        -------
            torch.Tensor
                Forecast of dims (batch, n_forecasts, no_quantiles)
        """
        # Turnaround to avoid issues when the meta argument is None and meta_used_in_model
        if meta is None and self.meta_used_in_model:
            name_id_dummy = self.id_list[0]
            meta = OrderedDict()
            meta["df_name"] = [name_id_dummy for _ in range(inputs["time"].shape[0])]
            meta = torch.tensor([self.id_dict[i] for i in meta["df_name"]], device=self.device)

        components = {}
        additive_components = torch.zeros(
            size=(inputs["time"].shape[0], self.n_forecasts, len(self.quantiles)),
            device=self.device,
        )
        additive_components_nonstationary = torch.zeros(
            size=(inputs["time"].shape[0], inputs["time"].shape[1], len(self.quantiles)), device=self.device
        )
        multiplicative_components_nonstationary = torch.zeros(
            size=(inputs["time"].shape[0], inputs["time"].shape[1], len(self.quantiles)), device=self.device
        )

        trend = self.trend(t=inputs["time"], meta=meta)
        components["trend"] = trend

        if "seasonalities" in inputs:
            s = self.seasonality(s=inputs["seasonalities"], meta=meta)
            if self.config_seasonality.mode == "additive":
                additive_components_nonstationary += s
            elif self.config_seasonality.mode == "multiplicative":
                multiplicative_components_nonstationary += s
            components["seasonalities"] = s

        if "events" in inputs:
            if "additive" in inputs["events"].keys():
                additive_events = self.scalar_features_effects(
                    inputs["events"]["additive"], self.event_params["additive"]
                )
                additive_components_nonstationary += additive_events
                components["additive_events"] = additive_events
            if "multiplicative" in inputs["events"].keys():
                multiplicative_events = self.scalar_features_effects(
                    inputs["events"]["multiplicative"], self.event_params["multiplicative"]
                )
                multiplicative_components_nonstationary += multiplicative_events
                components["multiplicative_events"] = multiplicative_events

        if "regressors" in inputs:
            if "additive" in inputs["regressors"].keys():
                additive_regressors = self.future_regressors(inputs["regressors"]["additive"], "additive")
                additive_components_nonstationary += additive_regressors
                components["additive_regressors"] = additive_regressors
            if "multiplicative" in inputs["regressors"].keys():
                multiplicative_regressors = self.future_regressors(
                    inputs["regressors"]["multiplicative"], "multiplicative"
                )
                multiplicative_components_nonstationary += multiplicative_regressors
                components["multiplicative_regressors"] = multiplicative_regressors

        # stationarized input
        if "lags" in inputs:
            # combinde all non-stationary components over AR input range
            nonstationary_components = (  # dimensions - [batch, n_lags, median quantile]
                trend[:, : self.n_lags, 0]
                + additive_components_nonstationary[:, : self.n_lags, 0]
                + trend[:, : self.n_lags, 0].detach() * multiplicative_components_nonstationary[:, : self.n_lags, 0]
            )
            stationarized_lags = inputs["lags"] - nonstationary_components
            lags = self.auto_regression(lags=stationarized_lags)
            additive_components += lags
            components["lags"] = lags

        if "covariates" in inputs:
            covariates = self.forward_covar_net(covariates=inputs["covariates"])
            additive_components += covariates
            components["covariates"] = covariates

        # combine all non-stationary components over forecast range
        predictions_nonstationary = (
            trend[:, self.n_lags : inputs["time"].shape[1], :]
            + additive_components_nonstationary[:, self.n_lags : inputs["time"].shape[1], :]
            + trend[:, self.n_lags : inputs["time"].shape[1], :].detach()
            * multiplicative_components_nonstationary[:, self.n_lags : inputs["time"].shape[1], :]
        )
        prediction = predictions_nonstationary + additive_components  # dimensions - [batch, n_forecasts, no_quantiles]

        # check for crossing quantiles and correct them here
        if "predict_mode" in inputs.keys() and inputs["predict_mode"]:
            predict_mode = True
        else:
            predict_mode = False
        prediction_with_quantiles = self._compute_quantile_forecasts_from_diffs(prediction, predict_mode)

        # component calculation
        if compute_components_flag:
            components = self.compute_components(inputs, components, meta)
        else:
            components = None

        return prediction_with_quantiles, components

    def compute_components(self, inputs: Dict, components_raw: Dict, meta: Dict) -> Dict:
        """This method returns the values of each model component.
        Note
        ----
        Time input is required. Minimum model setup is a linear trend.
        Parameters
        ----------
            inputs : dict
                Model inputs, each of len(df) but with varying dimensions
                Note
                ----
                Contains the following data:
                Model Inputs
                    * ``time`` (torch.Tensor , loat), normalized time, dims: (batch, n_forecasts)
                    * ``lags`` (torch.Tensor, float), dims: (batch, n_lags)
                    * ``seasonalities`` (torch.Tensor, float), dict of named seasonalities (keys) with their features
                    (values), dims of each dict value (batch, n_forecasts, n_features)
                    * ``covariates`` (torch.Tensor, float), dict of named covariates (keys) with their features
                    (values), dims of each dict value: (batch, n_lags)
                    * ``events`` (torch.Tensor, float), all event features, dims (batch, n_forecasts, n_features)
                    * ``regressors``(torch.Tensor, float), all regressor features, dims (batch, n_forecasts, n_features)
            components_raw : dict
                components to be computed
        -------
            dict
                Containing forecast coomponents with elements of dims (batch, n_forecasts)
        """
        components = {}

        components["trend"] = components_raw["trend"][:, self.n_lags : inputs["time"].shape[1], :]
        if self.config_trend is not None and "seasonalities" in inputs:
            for name, features in inputs["seasonalities"].items():
                components[f"season_{name}"] = self.seasonality.compute_fourier(
                    features=features[:, self.n_lags : inputs["time"].shape[1], :], name=name, meta=meta
                )
        if self.n_lags > 0 and "lags" in inputs:
            components["ar"] = components_raw["lags"]
        if self.config_lagged_regressors is not None and "covariates" in inputs:
            # Combined forward pass
            all_covariates = components_raw["covariates"]
            # Calculate the contribution of each covariate on each forecast
            covar_attributions = self.covar_weights
            # Sum the contributions of all covariates
            covar_attribution_sum_per_forecast = reduce(
                torch.add, [torch.sum(covar, axis=1) for _, covar in covar_attributions.items()]
            ).to(all_covariates.device)
            for name in inputs["covariates"].keys():
                # Distribute the contribution of the current covariate to the combined forward pass
                # 1. Calculate the relative share of each covariate on the total attributions
                # 2. Multiply the relative share with the combined forward pass
                components[f"lagged_regressor_{name}"] = torch.multiply(
                    all_covariates,
                    torch.divide(
                        torch.sum(covar_attributions[name], axis=1).to(all_covariates.device),
                        covar_attribution_sum_per_forecast,
                    ).reshape(self.n_forecasts, len(self.quantiles)),
                )
        if (self.config_events is not None or self.config_holidays is not None) and "events" in inputs:
            if "additive" in inputs["events"].keys():
                components["events_additive"] = components_raw["additive_events"][
                    :, self.n_lags : inputs["time"].shape[1], :
                ]
            if "multiplicative" in inputs["events"].keys():
                components["events_multiplicative"] = components_raw["multiplicative_events"][
                    :, self.n_lags : inputs["time"].shape[1], :
                ]
            for event, configs in self.events_dims.items():
                mode = configs["mode"]
                indices = configs["event_indices"]
                if mode == "additive":
                    features = inputs["events"]["additive"][:, self.n_lags : inputs["time"].shape[1], :]
                    params = self.event_params["additive"]
                else:
                    features = inputs["events"]["multiplicative"][:, self.n_lags : inputs["time"].shape[1], :]
                    params = self.event_params["multiplicative"]
                components[f"event_{event}"] = self.scalar_features_effects(
                    features=features, params=params, indices=indices
                )
        if self.config_regressors.regressors is not None and "regressors" in inputs:
            if "additive" in inputs["regressors"].keys():
                components["future_regressors_additive"] = components_raw["additive_regressors"][
                    :, self.n_lags : inputs["time"].shape[1], :
                ]

            if "multiplicative" in inputs["regressors"].keys():
                components["future_regressors_multiplicative"] = components_raw["multiplicative_regressors"][
                    :, self.n_lags : inputs["time"].shape[1], :
                ]

            for regressor, configs in self.future_regressors.regressors_dims.items():
                mode = configs["mode"]
                index = []
                index.append(configs["regressor_index"])
                features = inputs["regressors"][mode]
                components[f"future_regressor_{regressor}"] = self.future_regressors(
                    features[:, self.n_lags : inputs["time"].shape[1], :], mode, indeces=index
                )

        return components

    def set_compute_components(self, compute_components_flag):
        self.compute_components_flag = compute_components_flag

    def loss_func(self, inputs, predicted, targets):
        loss = None
        # Compute loss. no reduction.
        loss = self.config_train.loss_func(predicted, targets)
        # Weigh newer samples more.
        loss = loss * self._get_time_based_sample_weight(t=inputs["time"][:, self.n_lags :])
        loss = loss.sum(dim=2).mean()
        # Regularize.
        if self.reg_enabled:
            steps_per_epoch = math.ceil(self.trainer.estimated_stepping_batches / self.trainer.max_epochs)
            progress_in_epoch = 1 - ((steps_per_epoch * (self.current_epoch + 1) - self.global_step) / steps_per_epoch)
            loss, reg_loss = self._add_batch_regularizations(loss, self.current_epoch, progress_in_epoch)
        else:
            reg_loss = torch.tensor(0.0, device=self.device)
        return loss, reg_loss

    def training_step(self, batch, batch_idx):
        inputs, targets, meta = batch
        # Global-local
        if self.meta_used_in_model:
            meta_name_tensor = torch.tensor([self.id_dict[i] for i in meta["df_name"]], device=self.device)
        else:
            meta_name_tensor = None
        # Run forward calculation
        predicted, _ = self.forward(inputs, meta_name_tensor)
        # Store predictions in self for later network visualization
        self.train_epoch_prediction = predicted
        # Calculate loss
        loss, reg_loss = self.loss_func(inputs, predicted, targets)

        # Optimization
        optimizer = self.optimizers()
        optimizer.zero_grad()
        self.manual_backward(loss)
        optimizer.step()

        scheduler = self.lr_schedulers()
        scheduler.step()

        # Manually track the loss for the lr finder
        self.log("train_loss", loss, on_step=False, on_epoch=True, prog_bar=True, logger=True)
        self.log("reg_loss", reg_loss, on_step=False, on_epoch=True, prog_bar=True, logger=True)

        # Metrics
        if self.metrics_enabled:
            predicted_denorm = self.denormalize(predicted[:, :, 0])
            target_denorm = self.denormalize(targets.squeeze(dim=2))
            self.log_dict(self.metrics_train(predicted_denorm, target_denorm), **self.log_args)
            self.log("Loss", loss, **self.log_args)
            self.log("RegLoss", reg_loss, **self.log_args)
        return loss

    def validation_step(self, batch, batch_idx):
        inputs, targets, meta = batch
        # Global-local
        if self.meta_used_in_model:
            meta_name_tensor = torch.tensor([self.id_dict[i] for i in meta["df_name"]], device=self.device)
        else:
            meta_name_tensor = None
        # Run forward calculation
        predicted, _ = self.forward(inputs, meta_name_tensor)
        # Calculate loss
        loss, reg_loss = self.loss_func(inputs, predicted, targets)
        # Metrics
        if self.metrics_enabled:
            predicted_denorm = self.denormalize(predicted[:, :, 0])
            target_denorm = self.denormalize(targets.squeeze(dim=2))
            self.log_dict(self.metrics_val(predicted_denorm, target_denorm), **self.log_args)
            self.log("Loss_val", loss, **self.log_args)
            self.log("RegLoss_val", reg_loss, **self.log_args)

    def test_step(self, batch, batch_idx):
        inputs, targets, meta = batch
        # Global-local
        if self.meta_used_in_model:
            meta_name_tensor = torch.tensor([self.id_dict[i] for i in meta["df_name"]], device=self.device)
        else:
            meta_name_tensor = None
        # Run forward calculation
        predicted, _ = self.forward(inputs, meta_name_tensor)
        # Calculate loss
        loss, reg_loss = self.loss_func(inputs, predicted, targets)
        # Metrics
        if self.metrics_enabled:
            predicted_denorm = self.denormalize(predicted[:, :, 0])
            target_denorm = self.denormalize(targets.squeeze(dim=2))
            self.log_dict(self.metrics_val(predicted_denorm, target_denorm), **self.log_args)
            self.log("Loss_test", loss, **self.log_args)
            self.log("RegLoss_test", reg_loss, **self.log_args)

    def predict_step(self, batch, batch_idx, dataloader_idx=0):
        inputs, _, meta = batch
        # Global-local
        if self.meta_used_in_model:
            meta_name_tensor = torch.tensor([self.id_dict[i] for i in meta["df_name"]], device=self.device)
        else:
            meta_name_tensor = None
        # Add predict_mode flag to dataset
        inputs["predict_mode"] = True
        # Run forward calculation
        prediction, components = self.forward(inputs, meta_name_tensor, self.compute_components_flag)
        return prediction, components

    def configure_optimizers(self):
        # Optimizer
        optimizer = self._optimizer(self.parameters(), lr=self.learning_rate, **self.config_train.optimizer_args)

        # Scheduler
        lr_scheduler = self._scheduler(
            optimizer,
            max_lr=self.learning_rate,
            total_steps=self.trainer.estimated_stepping_batches,
            **self.config_train.scheduler_args,
        )

        return {"optimizer": optimizer, "lr_scheduler": lr_scheduler}

    def _get_time_based_sample_weight(self, t):
        weight = torch.ones_like(t)
        if self.config_train.newer_samples_weight > 1.0:
            end_w = self.config_train.newer_samples_weight
            start_t = self.config_train.newer_samples_start
            time = (t.detach() - start_t) / (1.0 - start_t)
            time = torch.maximum(torch.zeros_like(time), time)
            time = torch.minimum(torch.ones_like(time), time)  # time = 0 to 1
            time = np.pi * (time - 1.0)  # time =  -pi to 0
            time = 0.5 * torch.cos(time) + 0.5  # time =  0 to 1
            # scales end to be end weight times bigger than start weight
            # with end weight being 1.0
            weight = (1.0 + time * (end_w - 1.0)) / end_w
        return weight.unsqueeze(dim=2)  # add an extra dimension for the quantiles

    def _add_batch_regularizations(self, loss, epoch, progress):
        """Add regularization terms to loss, if applicable
        Parameters
        ----------
            loss : torch.Tensor, scalar
                current batch loss
            epoch : int
                current epoch number
            progress : float
                progress within the epoch, between 0 and 1
        Returns
        -------
            loss, reg_loss
        """
        delay_weight = self.config_train.get_reg_delay_weight(epoch, progress)

        reg_loss = torch.zeros(1, dtype=torch.float, requires_grad=False, device=self.device)
        if delay_weight > 0:
            # Add regularization of AR weights - sparsify
            if self.max_lags > 0 and self.config_ar.reg_lambda is not None:
                reg_ar = self.config_ar.regularize(self.ar_weights)
                reg_ar = torch.sum(reg_ar).squeeze() / self.n_forecasts
                reg_loss += self.config_ar.reg_lambda * reg_ar

            # Regularize trend to be smoother/sparse
            l_trend = self.config_trend.trend_reg
            if self.config_trend.n_changepoints > 0 and l_trend is not None and l_trend > 0:
                reg_trend = reg_func_trend(
                    weights=self.trend.get_trend_deltas,
                    threshold=self.config_train.trend_reg_threshold,
                )
                reg_loss += l_trend * reg_trend

            # Regularize seasonality: sparsify fourier term coefficients
            if self.config_seasonality:
                l_season = self.config_seasonality.reg_lambda
                if self.seasonality.season_dims is not None and l_season is not None and l_season > 0:
                    for name in self.seasonality.season_params.keys():
                        reg_season = reg_func_season(self.seasonality.season_params[name])
                        reg_loss += l_season * reg_season

            # Regularize events: sparsify events features coefficients
            if self.config_events is not None or self.config_holidays is not None:
                reg_events_loss = reg_func_events(self.config_events, self.config_holidays, self)
                reg_loss += reg_events_loss

            # Regularize regressors: sparsify regressor features coefficients
            if self.config_regressors.regressors is not None:
                reg_regressor_loss = reg_func_regressors(self.config_regressors.regressors, self)
                reg_loss += reg_regressor_loss

        trend_glocal_loss = torch.zeros(1, dtype=torch.float, requires_grad=False)
        # Glocal Trend
        if self.config_trend is not None:
            if self.config_trend.trend_global_local == "local" and self.config_trend.trend_local_reg:
                trend_glocal_loss = reg_func_trend_glocal(
                    self.trend.trend_k0, self.trend.trend_deltas, self.config_trend.trend_local_reg
                )
                reg_loss += trend_glocal_loss
        # Glocal Seasonality
        if self.config_seasonality is not None:
            if (
                self.config_seasonality.global_local in ["local", "glocal"]
                and self.config_seasonality.seasonality_local_reg
            ):
                seasonality_glocal_loss = reg_func_seasonality_glocal(
                    self.seasonality.season_params, self.config_seasonality.seasonality_local_reg
                )
                reg_loss += seasonality_glocal_loss
        loss = loss + reg_loss
        return loss, reg_loss

    def denormalize(self, ts):
        """
        Denormalize timeseries
        Parameters
        ----------
            target : torch.Tensor
                ts tensor
        Returns
        -------
            denormalized timeseries
        """
        if self.config_normalization.global_normalization:
            shift_y = (
                self.config_normalization.global_data_params["y"].shift
                if self.config_normalization.global_normalization and not self.config_normalization.normalize == "off"
                else 0
            )
            scale_y = (
                self.config_normalization.global_data_params["y"].scale
                if self.config_normalization.global_normalization and not self.config_normalization.normalize == "off"
                else 1
            )
            ts = scale_y * ts + shift_y
        return ts

    def train_dataloader(self):
        return self.train_loader


class FlatNet(nn.Module):
    """
    Linear regression fun
    """

    def __init__(self, d_inputs, d_outputs):
        # Perform initialization of the pytorch superclass
        super(FlatNet, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(d_inputs, d_outputs),
        )
        nn.init.kaiming_normal_(self.layers[0].weight, mode="fan_in")

    def forward(self, x):
        return self.layers(x)

    @property
    def ar_weights(self):
        return self.model.layers[0].weight


class DeepNet(nn.Module):
    """
    A simple, general purpose, fully connected network
    """

    def __init__(self, d_inputs, d_outputs, lagged_reg_layers=[]):
        # Perform initialization of the pytorch superclass
        super(DeepNet, self).__init__()
        self.layers = nn.ModuleList()
        for d_hidden_i in lagged_reg_layers:
            self.layers.append(nn.Linear(d_inputs, d_hidden_i, bias=True))
            d_inputs = d_hidden_i
        self.layers.append(nn.Linear(d_inputs, d_outputs, bias=True))
        for lay in self.layers:
            nn.init.kaiming_normal_(lay.weight, mode="fan_in")

    def forward(self, x):
        """
        This method defines the network layering and activation functions
        """
        activation = nn.functional.relu
        for i in range(len(self.layers)):
            if i > 0:
                x = activation(x)
            x = self.layers[i](x)
        return x

    @property
    def ar_weights(self):
        return self.layers[0].weight
