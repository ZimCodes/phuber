class Configurator:
    @staticmethod
    def order_filter(order, time):
        result = ''
        if order == "viewed":
            result += '&o=mv'
            if time:
                result += Configurator.__time_filter(time)
        elif order == 'longest':
            result += '&o=lg'
        elif order == 'top':
            result += '&o=tr'
            if time:
                result += Configurator.__time_filter(time)
        elif order == 'recent':
            result += '&o=mr'
        return result

    @staticmethod
    def __time_filter(time):
        if time == 'yearly':
            return '&t=y'
        elif time == 'monthly':
            return '&t=m'
        elif time == 'weekly':
            return '&t=w'
        elif time == 'daily':
            return '&t=t'

    @staticmethod
    def include_url_converter(include, categories):
        """
        Convert category specified by the user into one that can be used by the url
        :param include: the category to filter into the search
        :param categories: the category list of codes
        :return: the query parameter url to include into the search
        """
        result_str = ''
        if include in categories.keys():
            result_str = '&filter_category=%s' % categories[include]
        else:
            print('---------%s is not a Pornhub category! See "--category-list" for more info!' % include)
    
        return result_str
    
    @staticmethod
    def exclude_url_converter(exclude, categories):
        """
        Convert category(ies) specified by the user into one that can be used by the url
        :param exclude: the category(ies) to filter out of the search
        :param categories: the category list of codes
        :return: the query parameter url to include into the search
        """
        exclude_params_list = exclude.split(',')
        converted_filters = []
        separator = '-'

        for param in exclude_params_list:
            if param in categories.keys():
                converted_filters.append(categories[param])
            else:
                print('---------%s is not a Pornhub category! See "--category-list" for more info!' % param)

        result_str = separator.join(converted_filters)
        url_str = "&exclude_category=%s" % result_str
        return url_str
    
    @staticmethod
    def search_filters_cat(premium_only, include, exclude, categories):
        """
        Filters to use while searching for videos
        :param premium_only: show premium videos only (premium account required!)
        :param include: the category to include in search filter
        :param exclude: the category(ies) to exclude from search filter(max=10)
        :param categories: the category list of codes
        :return: the url query to use based on category search filter(s)
        """
        filter_url = []

        if premium_only:
            filter_url.append('&premium=1')

        if include:
            filter_url.append(Configurator.include_url_converter(include, categories))

        if exclude:
            filter_url.append(Configurator.exclude_url_converter(exclude,categories))

        filter_str = ''
        return filter_str.join(filter_url)
    
    @staticmethod
    def production_filter(production):
        """
        Filter the production of the videos
        :param production: the production of the video to use
        :return: the query parameter url for the production to filter into the search
        """
        prod_url = ''
        if production == 'prod':
            prod_url = '&p=professional'
        elif production == 'home':
            prod_url = '&p=homemade'

        return prod_url

    @staticmethod
    def duration_filter(minimum, maximum):
        """
        Filter the duration of the videos
        :param minimum: the minimum length of the videos
        :param maximum: the maximum length of the videos
        :return: the query parameter url of the duration to filter into the search
        """
        min_url = ''
        max_url = ''
        if maximum:
            max_url = '&max_duration=%d' % maximum
        if minimum:
            min_url = '&min_duration=%d' % minimum

        return min_url + max_url
