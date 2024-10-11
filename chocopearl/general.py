from datetime import timedelta

def input_yn(prompt='',yes='y',no='n',alt_yes=[],alt_no=[],wrong_input_msg=None):   
    """
        Prompts the user for a yes/no input and returns a boolean value based on the response.
        Parameters:
        prompt (str): The message displayed to the user. Default is an empty string.
        yes (str): The character representing a 'yes' response. Default is 'y'.
        no (str): The character representing a 'no' response. Default is 'n'.
        alt_yes (list): A list of alternative characters that also represent a 'yes' response. Default is an empty list.
        alt_no (list): A list of alternative characters that also represent a 'no' response. Default is an empty list.
        wrong_input_msg (str): The message displayed when the user provides an invalid input. Default is None, which sets a default message.
        Returns:
        bool: True if the user inputs a 'yes' response, False if the user inputs a 'no' response.
        Example:
        >>> input_yn(prompt='Do you want to continue?', yes='y', no='n', alt_yes=['yes'], alt_no=['no'])
        Do you want to continue? [y/n]: y
        True
        """
    alt_yes.append(yes)
    alt_no.append(no)
    if wrong_input_msg is None:
        wrong_input_msg='Type '+yes+' (yes) or '+no+' (no)\n'
    while True:
        flag=input(f'{prompt}[{yes}/{no}]: ')
        if flag in alt_yes:
            return True
        elif flag in alt_no:
            return False
        else:
            print(wrong_input_msg)
    
def input_options(options,options_msg='Options:',selection_msg='Enter the IDs of the options to select (separated by comas \',\' ): ',invalid_selection_msg='Invalid selection'):
    """
        Displays a list of options to the user and prompts them to select one or more options by entering their IDs.
        Args:
            options (list): A list of options to be displayed.
            options_msg (str, optional): The message to display before listing the options. Defaults to 'Options:'.
            selection_msg (str, optional): The message to prompt the user for their selection. Defaults to 'Enter the IDs of the options to select (separated by comas \',\' ): '.
            invalid_selection_msg (str, optional): The message to display if the user enters an invalid selection. Defaults to 'Invalid selection'.
        Returns:
            list: A list of selected options based on the user's input.
        """
    while True:
        print(options_msg)
        for id,o in zip(list(range(1,len(options)+1)),options):
            print(f"{id}| {str(o)} ")
        print("")
        selected_ids=input(selection_msg)
        selected_ids=selected_ids.split(',')
        try:
            selected_ids=[int(id) for id in selected_ids]
            selected_options=[options[id-1] for id in selected_ids]
            break
        except:
            print(invalid_selection_msg)
    return selected_options

def format_time(seconds,return_as='str'):
    """
        Convert a time duration from seconds into a formatted string or dictionary.

        Args:
            seconds (int): The total number of seconds to be converted.
            return_as (str, optional): The format of the returned value. 
                                       'str' for a formatted string (default), 
                                       'dict' for a dictionary with time components.

        Returns:
            str: A formatted string representing the time duration, e.g., "1D 2H 3M 4S".
            dict: A dictionary with keys 'D', 'H', 'M', 'S' representing days, hours, minutes, and seconds respectively.

        Example:
            >>> format_time(93784)
            '1D 2H 3M 4S'
            >>> format_time(93784, return_as='dict')
            {'D': 1, 'H': 2, 'M': 3, 'S': 4}
    """
    delta_t = timedelta(seconds=seconds)
    days = delta_t.days
    hours, remainder = divmod(delta_t.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    components = []
    if days:
        components.append(f"{days}D")
    if hours:
        components.append(f"{hours}H")
    if minutes:
        components.append(f"{minutes}M")
    if seconds:
        components.append(f"{seconds}S")
    if return_as=='str':
        time_string = " ".join(components)
        return time_string
    if return_as == 'dict':
        return {'D':days,'H':hours,'M':minutes,'S':seconds}
