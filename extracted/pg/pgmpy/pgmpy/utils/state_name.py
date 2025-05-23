class StateNameMixin:
    """
    This class is inherited by classes which deal with state names of variables.
    The state names are stored in instances of `StateNameMixin`. The conversion between
    state number and names are also handled by methods in this class.
    """

    def store_state_names(self, variables, cardinality, state_names):
        """
        Initialize an instance of StateNameMixin.

        Example
        -------
        >>> import numpy as np
        >>> from pgmpy.factors.discrete import DiscreteFactor
        >>> sn = {'speed': ['low', 'medium', 'high'],
        ...       'switch': ['on', 'off'],
        ...       'time': ['day', 'night']}
        >>> phi = DiscreteFactor(variables=['speed', 'switch', 'time'],
        ...                      cardinality=[3, 2, 2],
        ...                      values=np.ones(12),
        ...                      state_names=sn)
        >>> print(phi.state_names)
        """
        if state_names:
            for key, value in state_names.items():
                if not isinstance(value, (list, tuple)):
                    raise ValueError(
                        "The state names must be for the form: {variable: list_of_states}"
                    )
                elif not len(set(value)) == len(value):
                    raise ValueError(f"Repeated statenames for variable: {key}")

            # Make a copy, so that the original object doesn't get modified after operations.
            self.state_names = state_names.copy()
            # Create maps for easy access to specific state names of state numbers.
            if state_names:
                self.name_to_no = {}
                self.no_to_name = {}
                for key, values in self.state_names.items():
                    self.name_to_no[key] = {
                        name: no for no, name in enumerate(self.state_names[key])
                    }
                    self.no_to_name[key] = {
                        no: name for no, name in enumerate(self.state_names[key])
                    }
        else:
            self.state_names = {
                var: list(range(int(cardinality[index])))
                for index, var in enumerate(variables)
            }
            self.name_to_no = {
                var: {i: i for i in range(int(cardinality[index]))}
                for index, var in enumerate(variables)
            }
            self.no_to_name = self.name_to_no.copy()

    def get_state_names(self, var, state_no):
        """
        Given `var` and `state_no` returns the state name.
        """
        if self.state_names:
            return self.no_to_name[var][state_no]
        else:
            return state_no

    def get_state_no(self, var, state_name):
        """
        Given `var` and `state_name` return the state number.
        """
        if self.state_names:
            try:
                return self.name_to_no[var][state_name]
            except KeyError:
                raise KeyError(
                    f"state: {state_name} is an unknown for variable: {var}. It must be one of {list(self.name_to_no[var].keys())}"
                )
        else:
            return state_name

    def add_state_names(self, phi1):
        """
        Updates the attributes of this class with another factor `phi1`.
        Ensures state name consistency.

        Parameters
        ----------
        phi1: Instance of pgmpy.factors.DiscreteFactor
            The factor whose states and variables need to be added.
        """
        # Process all state names in a single loop
        for var in phi1.state_names:
            if var in self.state_names:
                # Check for conflicts between existing state names
                if self.state_names[var] != phi1.state_names[var]:
                    # One has strings and the other has numeric values - prioritize strings
                    self_has_strings = any(
                        isinstance(s, str) and not s.isdigit()
                        for s in self.state_names[var]
                    )
                    phi1_has_strings = any(
                        isinstance(s, str) and not s.isdigit()
                        for s in phi1.state_names[var]
                    )

                    # Keep string-based state names over numeric ones
                    if self_has_strings and not phi1_has_strings:
                        continue  # Keep current string-based state names
                    elif not self_has_strings and phi1_has_strings:
                        self.state_names[var] = phi1.state_names[var]
                        if var in phi1.name_to_no:
                            self.name_to_no[var] = phi1.name_to_no[var]
                        if var in phi1.no_to_name:
                            self.no_to_name[var] = phi1.no_to_name[var]
                    else:
                        # Both have similar types but different values - raise error
                        raise ValueError(
                            f"State name conflict detected for variable '{var}'.\n"
                            f"First factor has states: {self.state_names[var]}\n"
                            f"Second factor has states: {phi1.state_names[var]}\n"
                            f"When the same variable appears in multiple factors, "
                            f"the state names must be identical. Please ensure consistent "
                            f"state naming across your model."
                        )
            else:
                # No conflict - add the new state names
                self.state_names[var] = phi1.state_names[var]
                if var in phi1.name_to_no:
                    self.name_to_no[var] = phi1.name_to_no[var]
                if var in phi1.no_to_name:
                    self.no_to_name[var] = phi1.no_to_name[var]

    def del_state_names(self, var_list):
        """
        Deletes the state names for variables in var_list
        """
        for var in var_list:
            del self.state_names[var]
            del self.name_to_no[var]
            del self.no_to_name[var]
