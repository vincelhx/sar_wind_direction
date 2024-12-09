import numpy as np


def draw_vector(ax, origin, vector, color, label=None, extend=False):
    """
    Draw a vector from origin with a given color and optionally add a label

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The ax to draw the vector on

    origin : tuple
        The origin of the vector

    vector : tuple
        The vector to draw

    color : str
        The color of the vector

    label : str
        The label to add to the end of the vector

    extend : bool
        If True, the vector is extended from the origin 

    Results
    -------
    quiver : matplotlib.quiver.Quiver
        The quiver object representing the vector

    text : matplotlib.text.Text
        The text object representing the label
    """

    if extend:
        # Extend the vector in both directions
        extended_vector = np.array(vector) * 2
        # Adjust origin to extend backwards
        origin = np.array(origin) - np.array(vector)
        quiver = ax.quiver(*origin, *extended_vector, color=color,
                           scale=1, scale_units='xy', angles='xy', width=0.003)

        if label:
            # position the label at the end of the initial vector, not the extended
            end_point = np.array(origin) + np.array(extended_vector)
            text = ax.text(end_point[0], end_point[1], label, color=color,
                           verticalalignment='bottom', horizontalalignment='right')
            return quiver, text
    else:
        quiver = ax.quiver(*origin, *vector, color=color,
                           scale=1, scale_units='xy', angles='xy', width=0.003)

        if label:
            # position the label at the end of the initial vector, not the extended
            end_point = np.array(origin) + np.array(vector)
            text = ax.text(end_point[0], end_point[1], label, color=color,
                           verticalalignment='bottom', horizontalalignment='right')
            return quiver, text
    return quiver, None


def draw_angle(ax, center, start_angle, extent, radius=0.5, color='green', linewidth=1, clockwise=False):
    """
    Draw an angle arc from 'start_angle' with an extent in degrees, ending with a smooth arrow that appears
    as a natural continuation of the arc.


    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The ax to draw the vector on

    center : tuple
        The origin of the arc

    start_angle : float
        The starting angle of the arc in degrees in trigonometeric convention (0° is East, 90° is North)

    extent : float
        The extent of the arc in degrees

    radius : float
        The radius of the arc

    color : str 
        The color of the arc

    linewidth : float
        The width of the arc

    clockwise : bool
        If True, the arc is drawn clockwise, otherwise it is drawn counter-clockwise

    Results
    -------
    arc : matplotlib.lines.Line2D
        The arc object representing the angle

    arrow : matplotlib.patches.FancyArrowPatch
        The arrow object representing the end of the arc

    text : matplotlib.text.Text
        The text object representing the angle label   
    """

    # Convert angles from degrees to radians
    start_angle_rad = np.radians(start_angle)
    end_angle_rad = np.radians(
        start_angle + extent) if not clockwise else np.radians(start_angle - extent)

    # Generate theta for the arc
    theta = np.linspace(start_angle_rad, end_angle_rad, num=300)

    # Calculate the coordinates of the arc
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    # Plot the arc
    arc = ax.plot(x, y, color=color, linewidth=linewidth)[0]

    # Adding arrow at the end of the arc
    arrow_length = 0.01 * radius  # making the arrow length proportional to the radius
    if clockwise:
        arrow_dx = arrow_length * np.cos(-np.pi/2+end_angle_rad)
        arrow_dy = arrow_length * np.sin(-np.pi/2+end_angle_rad)
    else:
        arrow_dx = arrow_length * np.cos(np.pi/2+end_angle_rad)
        arrow_dy = arrow_length * np.sin(np.pi/2+end_angle_rad)

    # Calculate the arrow's base_meteo point so it looks like it's continuing the arc
    arrow_base_x = x[-5] - arrow_dx
    arrow_base_y = y[-5] - arrow_dy

    # Draw arrow
    arrow = ax.arrow(arrow_base_x, arrow_base_y, arrow_dx, arrow_dy,
                     head_width=0.05, head_length=0.05, fc=color, ec=color)

    # Calculate midpoint for the angle label
    mid_index = len(theta) // 2
    x2 = (center[0] + (radius+0.05) * np.cos(theta))
    y2 = (center[1] + (radius+0.05) * np.sin(theta))
    text_x = x2[mid_index]
    text_y = y2[mid_index]

    angle_text = f'{abs(extent)}°'
    text = ax.text(text_x, text_y, angle_text, color=color, fontsize=12,
                   horizontalalignment='center', verticalalignment='center')

    return arc, arrow, text
