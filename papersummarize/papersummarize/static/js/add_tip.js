class DummyInput extends React.Component {
    render() {
        return React.createElement('span', null, null);
    }
}

class TextInput extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(event) {
        var data = event.target.value;
        var isValid = this.validate(data);
        if (!isValid) {
            var helpText = 'Must be less than 100 characters.';
        } else {
            var helpText = '';
        }
        this.props.handleDataChange(data, isValid, helpText);
    }

    validate(data) {
        return data.length < 100;
    }

    render() {
        return React.createElement('input', {name: 'body', className: 'form-control', onChange: this.handleChange, value: this.props.semanticData});
    }
}

class URLInput extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this)
    }

    validate(data) {
        try {
            var url = new URL(data);
            return true;
        } catch (e) {
            return false;
        }
    }

    handleChange(event) {
        var data = event.target.value;
        var isValid = this.validate(data);
        if (!isValid) {
            var helpText = 'Please use a valid url (hint: include https://).';
        } else {
            var helpText = '';
        }
        this.props.handleDataChange(data, isValid, helpText);
    }

    render() {
        return React.createElement('input', {name: 'body', className: 'form-control', placeholder: 'Enter github url.', onChange: this.handleChange, value: this.props.semanticData });
    }
}

class TipSuggestions extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return React.createElement('div', null, 
            React.createElement('p', null, 'Choose from popular categories:'),
            React.createElement('ul', null,
                React.createElement('li', null,
                    React.createElement('a', {href: '#', onClick: function() {this.props.onClick('github')}.bind(this)}, 'github')
                ),
                React.createElement('li', null,
                    React.createElement('a', {href: '#', onClick: function() {this.props.onClick('other')}.bind(this)}, 'other')
                )
            )
        );
    }
}

class TipForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { semanticData: '', semanticCategory: 'default', isValid: false, helpText: ''};

        this.handleCategoryChange = this.handleCategoryChange.bind(this);
        this.handleDataChange = this.handleDataChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.changeCategory = this.changeCategory.bind(this);
    }

    changeCategory(category) {
        this.setState({ semanticData: '', semanticCategory: category, isValid: false, helpText: '' });
    }

    handleCategoryChange(event) {
        var category = event.target.value;
        this.changeCategory(category);
    }

    handleDataChange(data, isValid, helpText) {
        this.setState({ semanticData: data, isValid: isValid, helpText: helpText });
    }

    handleSubmit(event) {
        if (!this.state.isValid) {
            event.preventDefault();
        }
    }

    createSemanticInputNode(semanticData, semanticCategory) {
        var props = {handleDataChange: this.handleDataChange, semanticData: semanticData};
        switch(semanticCategory) {
            case 'github':
                return React.createElement(URLInput, props);
            case 'other':
                return React.createElement(TextInput, props);
            default:
                return React.createElement(DummyInput, props);
        }
    }

    render() {
        var semanticInputNode = this.createSemanticInputNode(this.state.semanticData, this.state.semanticCategory);
        var hasErrorClass = this.state.isValid ? '' : ' has-error';
        var semanticInputNodes = [semanticInputNode];
        if (this.state.helpText) {
            var semanticInputHelpNode = React.createElement('span', {className: 'help-block'}, this.state.helpText);
            semanticInputNodes.push(semanticInputHelpNode);
        }

        return React.createElement('div', null,
            React.createElement(TipSuggestions, {onClick: this.changeCategory}, null),
            React.createElement('form', {className: 'TipForm', onSubmit: this.handleSubmit, action: '{{ save_url }}'},
                React.createElement('div', {className: 'form-group semantic-input' + hasErrorClass}, semanticInputNodes),
                React.createElement('div', {className: 'form-group semantic-category'},
                    React.createElement('span', null, 'Category: '),
                    React.createElement('span', null,
                        React.createElement('select', {onChange: this.handleCategoryChange, value: this.state.semanticCategory},
                            React.createElement('option', {disabled: true, value: 'default'}, ' -- select an option -- '),
                            React.createElement('option', {value: 'github'}, 'Github URL'),
                            React.createElement('option', {value: 'other'}, 'Other')
                        )
                    )
                ),
                React.createElement('div', {className: 'form-group'},
                    React.createElement('button', {className: 'btn btn-default', name: 'form.submitted'}, `Submit`),
                )
            )
        );
    }
}

ReactDOM.render(
    React.createElement(TipForm, null, null),
    document.getElementById('react-root')
);
