from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Channel, Category, Language
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AddChannelForm
from .telegram_info_scrap import get_soup_telegram, get_image, get_description, get_members, get_title
from django.forms import HiddenInput


class CategoriesListView(generic.ListView):
    model = Category
    template_name = 'channels/home.html'
    context_object_name = 'categories'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     my_retults = Category.objects.filter(name=self.kwargs['name'])
    #     for i in my_retults:
    #         print(i)
    #
    #     return data


def about(request):
    return render(request, 'channels/about.html')


def contact(request):
    return render(request, 'channels/contact.html')


class ChannelListView(generic.ListView):
    model = Channel
    template_name = 'channels/category.html'
    context_object_name = 'channels'

    def get_queryset(self):
        my_retults = Category.objects.filter(name=self.kwargs['name']).values_list('id', flat=True)

        return Channel.objects.filter(category=my_retults[0])

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)

        first_row = []
        second_row = []
        third_row = []
        fourth_row = []
        add_three = False
        add_two = False
        add_one = False
        add_none = False

        for i in range(1, 100):
            var1 = 1 + ((i - 1)*4)
            first_row.append(var1)
            var2 = 2 + ((i - 1)*4)
            second_row.append(var2)
            var3 = 3 + ((i - 1)*4)
            third_row.append(var3)
            var4 = 4 + ((i - 1)*4)
            fourth_row.append(var4)

        data["first_row"] = first_row
        data["second_row"] = second_row
        data["third_row"] = third_row
        data["fourth_row"] = fourth_row

        my_retults = Category.objects.filter(name=self.kwargs['name']).values_list('id', flat=True)
        size_len = Channel.objects.filter(category=my_retults[0]).count()

        # print("SIZE ", size_len)

        if int(size_len) in first_row:
            add_three = True
        if int(size_len) in second_row:
            add_two = True
        if int(size_len) in third_row:
            add_one = True
        if int(size_len) in fourth_row:
            add_none = True

        print("add_three: ",add_three,"add_two: ",add_two,"add_one",add_one,"add_none",add_none)

        data['add_three'] = add_three
        data['add_two'] = add_two
        data['add_one'] = add_one
        data['add_none'] = add_none

        data['category_name'] = self.kwargs['name']

        return data


class ChannelDetailView(generic.DetailView):
    model = Channel
    template_name = 'channels/channel.html'


@login_required
def add_channel(request):
    if request.method == 'POST':
        ch_usrname = request.POST.get('channel_username')
        channel_instance = get_object_or_404(Channel, channel_username=ch_usrname)
        form = AddChannelForm(request.POST, instance=channel_instance)
        if form.is_valid():
            # print(request.user)
            # form.author = request.user
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('channels-home')
    else:
        show_second_form = False
        form = AddChannelForm()
        ch = None
        error = False
        if 'q' in request.GET:
            channel_username = request.GET['q']
            if not channel_username:
                error = True
            else:
                show_second_form = True
                soup = get_soup_telegram(channel_username)
                title = get_title(soup)
                members = get_members(soup)
                description = get_description(soup)
                image = get_image(soup, channel_username)

                #channel_instance = get_object_or_404(Channel, channel_username=channel_username)
                try:
                    channel_instance = Channel.objects.get(channel_username=channel_username)
                except:
                    channel_instance = None

                if channel_instance:
                    form = AddChannelForm(instance=channel_instance)
                    ch = channel_instance

                    obj = form.save(commit=False)
                    obj.title = title
                    obj.subscribers = members
                    obj.image = image
                    obj.save()
                else:
                    ch = Channel.objects.create(
                        title=title,
                        channel_url='https://t.me/' + channel_username,
                        channel_username=channel_username,
                        image=image,
                        description=description,
                        subscribers=members,
                        language=Language.objects.get(pk=1),
                        category=Category.objects.get(pk=1),
                        author=User.objects.get(pk=1),
                    )

                    form = AddChannelForm(instance=ch)

    return render(request,
                  'channels/channel_add_form.html',
                  {"form": form, "added_channel": ch, "error": error, 'show_second_form': show_second_form}
                  )

